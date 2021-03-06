from typing import List
from src.core.Point import Point


class Trajectory:

    def __init__(self, points: List[Point]) -> None:
        self._points = points

    def is_timed(self) -> bool:
        return self._points[0].is_timed()

    @property
    def points(self) -> List[Point]:
        return self._points

    @points.setter
    def points(self, points: List[Point]) -> None:
        self._points = points
