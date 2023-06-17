import machine
import socket
import network
import time
from __buzzer import Buzzer


class WebServerManager:

    def __init__(self, ):

        # Configure Wlan
        self.__wlan = network.WLAN(network.AP_IF)
        self.__wlan.config(security=0, ssid="badaboomWifi")
        self.__wlan.active(True)

        # Wait for connect or fail
        wait = 30
        while wait > 0:
            if self.__wlan.status() < 0 or self.__wlan.status() >= 3:
                break
            wait -= 1
            print(f'waiting for connection: status {self.__wlan.status()}')
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
                self.__ip = ip
        except KeyboardInterrupt:
            machine.reset()

        self.__question_to_display = ['Badaboum!!!']
        self.__question_index = 0
        self.__tick_time = 2
        self.running = False

    def run(self, buzzer: Buzzer):
        self.__buzzer = buzzer
        self.running = True
        try:
            while True:
                self.__serve()
                time.sleep_ms(300)
        finally:
            print('shutting down web server')
            self.__connection.close()

    def update_webpage(self, questions:list[str],
                       tick_time:float):
        self.__tick_time = tick_time
        self.__question_index = 0
        self.__question_to_display = questions

    def __serve(self):

        client: socket.socket
        try:
            client, address = self.__connection.accept()
        except OSError as e:
            print(f'oserror: {e.args}')
            return
        self.get_webpage()
        try:
            request = client.recv(1024)
            try:
                request = request.split()[1]
            except IndexError:
                print("No request received")
                return
            client.send(self.__updated_html)
        except:
            print("Client connexion close")
            client.close()
            return
        finally:
            client.close()

    def get_webpage(self):
        print(f"{(self.__question_index)=}")
        self.__updated_html = """<!DOCTYPE html>
<html>
<META http-equiv=refresh content="2" charset="UTF-8">

<body style="background-color:black;">
  <p id="time_left" style="font-size:100px;color:red;text-align:center;"></p>
  <p id="questions" style="font-size:50px;color:red;text-align:center;font-family:Cursive;">super question</p>
  <script>
    setInterval(tick_tm, 1000);
    let s = 250;
    tick_tm();
    function tick_tm() {
      let sec_left_hour = s % 3600;
      let hrs = ((s - sec_left_hour) / 3600);
      let sec_left = sec_left_hour % 60;
      let min = (sec_left_hour - sec_left) / 60;
      document.getElementById("time_left").innerHTML = hrs.toString().padStart(
          2, "0") + ":" + min.toString().padStart(2, "0") + ":" + sec_left.toString().padStart(2, "0");
      s = s - 1;
    }
  </script>
</body>

</html>"""
# .format(self.__question_to_display[self.__question_index].encode("utf-8"),
#                   int(self.__tick_time*1000),
#                   self.__buzzer.get_time_left())

        self.__question_index = (
            self.__question_index+1) % (2*len(self.__question_to_display))

    @ staticmethod
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
