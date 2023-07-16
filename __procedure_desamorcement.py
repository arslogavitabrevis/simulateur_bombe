from machine import Pin, Timer
from __buzzer import Buzzer
from web_server import WebServerManager
from liste_des_etapes import liste_des_etapes
import time

class SequenceDesarmorcement:
    def __init__(self, web_server: WebServerManager, buzzer: Buzzer):

        # Variable globale pour l'étape
        self.__etape = 0

        self.__web_server = web_server
        self.__buzzer = buzzer

        # Define the inputs pins
        self.__cable_coupes = 0

        self.__pins = [Pin(i, mode=Pin.IN, pull=Pin.PULL_UP)
                       for i in range(1, 24)]
        self.__pins[0].irq(trigger=Pin.IRQ_FALLING, handler=self.__fermeture_capot)
        
    def __fermeture_capot(self, pin:Pin):
        self.__verification(True)
        time.sleep(0.5)
        for i, pin in enumerate(self.__pins):
            pin.irq(trigger=Pin.IRQ_RISING,
                    handler=lambda pin, pin_num=i: self.__gpio_interrup_callback(pin, pin_num))
        self.__timer = Timer()
        self.__timer.init(
            period=2500, callback=self.__callback_timer_verification)

    def __gpio_interrup_callback(self, pin: Pin, pin_number: int):
        if not self.__web_server.running:
            return
        pin_mask = 1 << pin_number
        if not self.__cable_coupes & pin_mask:
            self.__cable_coupes |= pin_mask
            self.__etape += 1
            self.__verification(update=True)

    def __callback_timer_verification(self, timer: Timer):
        if self.__web_server.running:
            self.__verification()

    def __verification(self, update=False):
        (pin_a_verifier,
         question,
         periode,
         nouveau_temps) = liste_des_etapes[self.__etape]

        # Si la pin a vérifier a été coupé
        if pin_a_verifier is not None and self.__pins[pin_a_verifier-1].value() == True:
            print("pin {} déconnecté".format(pin_a_verifier))
            self.__etape += 1
            if self.__etape >= len(liste_des_etapes):
                self.__etape = len(liste_des_etapes)-1
                return
            self.__verification(update=True)
            return
        if update:
            self.__buzzer.update_buzzer(
                refresh=periode, time_left=nouveau_temps)
            self.__web_server.update_webpage(
                questions=question, tick_time=periode)
