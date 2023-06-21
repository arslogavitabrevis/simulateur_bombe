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
        self.__q_idx_cooldown = False
        self.__tick_time = 2
        self.running = False

    def run(self, buzzer: Buzzer):
        self.__buzzer = buzzer
        self.__question_index_timer = machine.Timer()
        self.running = True
        try:
            while True:
                self.__serve()
                time.sleep_ms(300)
        finally:
            print('shutting down web server')
            self.__connection.close()

    def update_webpage(self, questions: list[str],
                       tick_time: float):
        self.__tick_time = tick_time
        self.__question_index = 0
        self.__question_to_display = questions

    def __cooldown_question_idx(self, timer: machine.Timer):
        self.__q_idx_cooldown = False

    def __serve(self):

        client: socket.socket
        try:
            client, address = self.__connection.accept()
        except OSError as e:
            print(f'oserror: {e.args}')
            return
        html_page = self.get_webpage()
        try:
            request = client.recv(1024)
            try:
                request = request.split()[1]
            except IndexError:
                print("No request received")
                return
            client.send(html_page)
        except:
            print("Client connexion close")
            client.close()
            return
        finally:
            client.close()

    def get_webpage(self):
        if not self.__q_idx_cooldown:
            self.__q_idx_cooldown = True
            self.__question_index = (
                self.__question_index+1) % len(self.__question_to_display)
            self.__question_index_timer.deinit()
            self.__question_index_timer.init(
                mode=machine.Timer.ONE_SHOT,
                period=1000, callback=self.__cooldown_question_idx)

        question = self.__question_to_display[self.__question_index]

        return """<!DOCTYPE html>
<html>
<META http-equiv=refresh content="2.5" charset="UTF-8">

<body style="background-color:black;">
  <p id="time_left" style="font-size:100px;color:red;text-align:center;"></p>
  <p{format} id="questions" style="font-size:50px;color:red;text-align:center;font-family:Cursive;">{}</p{format}>
  <script>
    setInterval(tick_tm, {});
    let s = {};
    tick_tm();
    function tick_tm() {}
      let sec_left_hour = s % 3600;
      let hrs = ((s - sec_left_hour) / 3600);
      let sec_left = sec_left_hour % 60;
      let min = (sec_left_hour - sec_left) / 60;
      document.getElementById("time_left").innerHTML = hrs.toString().padStart(
          2, "0") + ":" + min.toString().padStart(2, "0") + ":" + sec_left.toString().padStart(2, "0");
      s = s - 1;
    {}
  </script>
</body>

</html>""".format(question,
                  int(self.__tick_time*1000),
                  self.__buzzer.get_time_left(),
                  '{', '}',
                  format={True: "re", False: ""}['\n' in question])

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
