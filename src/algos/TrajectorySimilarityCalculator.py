from abc import ABC, abstractmethod
from src.core.Trajectory import Trajectory

from enum import Enum, unique


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

    @abstractmethod
    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError


class _DTWCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__("DTW Calculator")

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError


class _SDTWCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__("SDTW Calculator")

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError


class _HausdorffCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__("Hausdorff Calculator")

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError


@unique
class Calculator(Enum):
    DTW = _DTWCalculator()
    SDTW = _SDTWCalculator()
    HAUSDORFF = _HausdorffCalculator()
