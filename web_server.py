import machine
import socket
import network
import time
from __buzzer import Buzzer
import _thread
import utime


class WebServerManager:

    def __init__(self, buzzer: Buzzer, web_page_param_lock: _thread.LockType):

        self.__web_page_param_lock = web_page_param_lock
        self.__buzzer = buzzer

        # Configure Wlan
        self.__wlan = network.WLAN(network.AP_IF)
        self.__wlan.config(security=0, ssid="badaboomWifi")
        self.__wlan.active(True)

        with open("./page.html", "r") as f:
            self.__html_template: str = f.read()

        # Wait for connect or fail
        wait = 30
        while wait > 0:
            if self.__wlan.status() < 0 or self.__wlan.status() >= 3:
                break
            wait -= 1
            print('waiting for connection...')
            time.sleep(1)

        # Handle connection error
        if self.__wlan.status() != network.STAT_GOT_IP:
            raise RuntimeError('wifi connection failed')
        else:
            print('connected')
            ip = self.__wlan.ifconfig()[0]
            print('IP: ', ip)

        try:
            if ip is not None:
                self.__connection = self.__open_socket(ip)
                self.ip = ip
        except KeyboardInterrupt:
            machine.reset()

    def run(self):
        self.__question_to_display = ['Badaboum!!!']
        self.__question_index = 0
        self.__refresh = 2
        while True:
            self.__serve()
            utime.sleep_ms(200)

    def update_webpage(self, questions=None,
                       refresh=None,):

        self.__web_page_param_lock.acquire()
        if refresh is not None and refresh != self.__refresh:
            self.__refresh = refresh

        if questions is not None:
            self.__question_index = 0
            self.__question_to_display = questions
        else:
            self.__question_index = (
                self.__question_index+1) % len(self.__question_to_display)

        self.__updated_html = self.__html_template.replace(
            "[refresh]", f"{self.__refresh}"
        ).replace("[time]", self.__buzzer.encode_time_left()
                  ).replace("[question]", self.__question_to_display[self.__question_index])
        self.__web_page_param_lock.release()

    def __serve(self):
        
        client: socket.socket
        client, address = self.__connection.accept()

        try:
            request = client.recv(1024)
        except:
            print("Client connexion close")
            client.close()
            return

        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            print("No request received")
            return

        print("updating client")

        self.update_webpage()
        client.send(self.__updated_html)

        client.close()

    @staticmethod
    def __open_socket(ip):
        # Open a socket
        address = (ip, 80)
        connection = socket.socket()
        connection.bind(address)
        connection.listen(1)
        print(connection)
        return (connection)

    def __del__(self):
        print("Closing connection")
        self.__connection.close()
