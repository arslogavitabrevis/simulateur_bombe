from web_server import WebServerManager
from __procedure_desamorcement import SequenceDesarmorcement
from __buzzer import Buzzer

print("Démarrage de la bombe")


class SimulateurBombe:

    def __init__(self):

        self.__web_server = WebServerManager()
        self.__buzzer = Buzzer()

        self.__desamorcement = SequenceDesarmorcement(
            self.__web_server,
            self.__buzzer,)

        self.__web_server.run(self.__buzzer)


if __name__ == "__main__":
    simulateur_bombe = SimulateurBombe()
