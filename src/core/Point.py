class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __int__(self, x: float, y: float, time: float):
        self.__init__(x, y)
        self.time = time

    def is_timed(self) -> bool:
        return hasattr(self, 'time')
