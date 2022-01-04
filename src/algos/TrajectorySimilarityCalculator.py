from abc import ABC, abstractmethod
from src.core.Trajectory import Trajectory


class TrajectorySimilarityCalculator(ABC):

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        return self.name

    def needs_timed_trajectory(self) -> bool:
        return False

    @abstractmethod
    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError
