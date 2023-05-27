import machine
import socket
import network
import time


class WebServerManager:

    def __init__(self):

        # Configure Wlan
        self.__wlan = network.WLAN(network.AP_IF)
        self.__wlan.config(security=0, ssid="badaboomWifi")
        self.__wlan.active(True)

        with open("./page.html", "r") as f:
            self.__html_template: str = f.read()

        # Wait for connect or fail
        wait = 20
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

        # Activer une pin de sortie pour le buzzer
        PREMIERE_PIN = 0
        self.__buzzer_pin = machine.Pin(PREMIERE_PIN, machine.Pin.OUT)
        self.__buzzer_pin.low()

    def run(self):
        self.__time_left_s = "30:00"
        self.__question_to_display = ['Badaboum!!!']
        self.__question_index = 0
        self.__refresh = 2
        self.update_webpage()
        self.__timer = machine.Timer()
        self.__timer.init(period=self.__refresh*1000, callback=self.__serve)

    def update_webpage(self, question=None,
                       refresh=None,
                       time_left_s=None,):
        
        if refresh is not None:
            self.__refresh = refresh
            self.__timer.deinit()
            self.__timer.init(period=self.__refresh *
                              1000, callback=self.__serve)

        if time_left_s is not None:
            self.__time_left_s = f"{int(time_left_s/60):02d}:{time_left_s%60:02d}"

        if question is not None:
            self.__question_index = 0
            self.__question_to_display = question
        else:
            self.__question_index = (
                self.__question_index+1) % len(self.__question_to_display)

        self.__updated_html = self.__html_template.replace(
            "[refresh]", f"{self.__refresh}"
        ).replace("[time]", self.__time_left_s).replace("[question]", self.__question_to_display[self.__question_index])

    def __serve(self, timer: machine.Timer):
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

        print(request)
        print("updating client")

        self.update_webpage()
        client.send(self.__updated_html)

        client.close()

        self.__buzzer_pin.high()
        self.__timer_buzzer = machine.Timer(
            mode=machine.Timer.ONE_SHOT,
            period=200,
            callback=self.__stop_buzzer)

    def __stop_buzzer(self, timer: machine.Timer):
        timer.deinit()
        self.__buzzer_pin.low()

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
