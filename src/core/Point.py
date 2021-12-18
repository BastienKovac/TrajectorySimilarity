class Point:

    def __init__(self, x: float, y: float, time: float = -1) -> None:
        self._x = x
        self._y = y
        self._time = time

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float) -> None:
        self._x = x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float) -> None:
        self._y = y

    @property
    def time(self) -> float:
        return self._time

    @time.setter
    def time(self, time: float) -> None:
        self._time = time

    def is_timed(self) -> bool:
        return self.time != -1
