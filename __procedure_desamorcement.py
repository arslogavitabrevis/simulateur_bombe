from machine import Pin, Timer
from __buzzer import Buzzer
from web_server import WebServerManager
from liste_des_etapes import liste_des_etapes


class SequenceDesarmorcement:
    def __init__(self, web_server: WebServerManager, buzzer: Buzzer):

        # Variable globale pour l'étape
        self.__etape = 0

        self.__web_server = web_server
        self.__buzzer = buzzer

        # Define the inputs pins
        self.__cable_coupes = 0
        self.__pins = [Pin(i, Pin.IN, Pin.PULL_DOWN)
                       for i in range(1, len(liste_des_etapes)+1)]
        for i, pin in enumerate(self.__pins):
            pin.irq(trigger=Pin.IRQ_FALLING,
                    handler=lambda pin, pin_num=i: self.__gpio_interrup_callback(pin, pin_num))

        # Initialiser la bombe à l'étape initiale
        self.__verification(update=True)

        # Faire une timer pour vérifier l'étape au secondes
        # au cas ou l'interrupt serait manqué
        self.__timer = Timer()
        self.__timer.init(
            period=1500, callback=self.__callback_timer_verification)

    def __gpio_interrup_callback(self, pin: Pin, pin_number: int):
        pin_mask = 1 << pin_number
        if not self.__cable_coupes & pin_mask:
            self.__cable_coupes |= pin_mask
            self.__etape += 1
            self.__verification(update=True)

    def __callback_timer_verification(self, timer: Timer):
        self.__verification()

    def __verification(self, update=False):
        (pin_a_verifier,
         question,
         periode,
         nouveau_temps) = liste_des_etapes[self.__etape]

        # Si la pin a vérifier a été coupé
        if self.__pins[pin_a_verifier-1].value() == False:
            print("pin {} déconnecté".format(pin_a_verifier))
            self.__etape += 1
            if self.__etape >= len(liste_des_etapes):
                self.__etape = len(liste_des_etapes)-1
                return
            self.__verification(update=True)
            return
        print("pin {} value: {}".format(pin_a_verifier,
              self.__pins[pin_a_verifier].value()))
        if update:
            self.__buzzer.update_buzzer(
                refresh=periode, time_left=nouveau_temps)
            self.__web_server.update_webpage(
                questions=question, refresh=periode)
