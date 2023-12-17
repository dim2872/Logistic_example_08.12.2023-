import datetime


class Route:
    _start = None
    _end = None
    _ets = datetime.time()
    _eta = datetime.time()

    def __init__(self, start, end, ets, eta):
        self._start = start
        self._end = end
        self._ets = ets
        self._eta = eta
        self._estimated_time = (datetime.datetime.combine(datetime.date.today(), eta)
                                - datetime.datetime.combine(datetime.date.today(), ets))

    def get_points(self):
        return self._start, self._end

    def get_timings(self):
        return self._ets, self._eta

    def __str__(self):
        return f"Путь из {self._start.get_name()} в {self._end.get_name()}, время поездки: {self._estimated_time}"

    def __repr__(self):
        return f"[{self._start.__repr__()}:{self._ets} -> {self._end.__repr__()}:{self._eta}]"