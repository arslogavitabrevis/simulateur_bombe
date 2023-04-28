import machine
import utime
import machine
from web_server import WebServerManager
from __procedure_desamorcement import SequenceDesarmorcement

print("hello")

class SimulateurBombe:

    def __init__(self):
        self.__web_server = WebServerManager()

        self.__web_server.run()
        
        self.__desamorcement = SequenceDesarmorcement(
            fonction_mise_a_jour=self.__web_server.update_webpage
        )

if __name__ == "__main__":
    print(__name__)
    simulateur_bombe = SimulateurBombe()
