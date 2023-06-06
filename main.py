import _thread
from web_server import WebServerManager
from __procedure_desamorcement import SequenceDesarmorcement
from __buzzer import Buzzer

print("Démarrage de la bombe")

class SimulateurBombe:

    def __start_web_server(self):
        self.__web_server = WebServerManager(
            self.__buzzer, self.__web_page_param_lock)
        self.__web_server.run()

    def __init__(self):
        self.__time_left_lock = _thread.allocate_lock()
        self.__web_page_param_lock = _thread.allocate_lock()

        self.__buzzer = Buzzer(self.__time_left_lock)

        _thread.start_new_thread(self.__start_web_server, ())

        self.__desamorcement = SequenceDesarmorcement(
            web_server=self.__web_server,
            buzzer=self.__buzzer,)


if __name__ == "__main__":
    simulateur_bombe = SimulateurBombe()
