import machine


class Buzzer:

    def __init__(self) -> None:

        self.__time_left_s = 1800  # s

        self.__refresh = 2000  # ms

        # Activer une pin de sortie pour le buzzer
        self.__buzzer_pin = machine.Pin(0, machine.Pin.OUT)
        self.__buzzer_pin.low()

        self.__tick_timer = machine.Timer()
        self.__tick_timer.init(period=self.__refresh,
                               callback=self.__start_buzzer)

    def update_buzzer(self, refresh=None, time_left=None):
        if refresh is not None:
            new_refresh = int(refresh*1000)
            if new_refresh != self.__refresh:
                self.__refresh = new_refresh
                self.__tick_timer.deinit()
                self.__tick_timer.init(
                    period=self.__refresh, callback=self.__start_buzzer)

        if time_left is not None:
            self.__time_left_s = time_left

    def get_time_left(self) -> int:
        return self.__time_left_s

    def __start_buzzer(self, timer: machine.Timer):
        self.__time_left_s = max(0, self.__time_left_s-1)
        machine.Timer(
            mode=machine.Timer.ONE_SHOT,
            period=min(400, int(self.__refresh/2)),
            callback=self.__stop_buzzer)
        self.__buzzer_pin.high()

    def __stop_buzzer(self, timer: machine.Timer):
        timer.deinit()
        self.__buzzer_pin.low()
