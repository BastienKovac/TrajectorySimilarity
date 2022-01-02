from abc import ABC, abstractmethod
from src.core.Trajectory import Trajectory

from enum import Enum

DTW_NAME = "DTW Calculator"
SDTW_NAME = "SDTW Calculator"
HAUSDORFF_NAME = "Hausdorff Calculator"


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


class _DTWCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__(DTW_NAME)

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError


class _SDTWCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__(SDTW_NAME)

    def needs_timed_trajectory(self) -> bool:
        return True

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError


class _HausdorffCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__(HAUSDORFF_NAME)

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError


class FinalMeta(type(Enum), type(ABC)):
    pass


class Calculator(TrajectorySimilarityCalculator, Enum, metaclass=FinalMeta):
    DTW = _DTWCalculator()
    SDTW = _SDTWCalculator()
    HAUSDORFF = _HausdorffCalculator()

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        return self.compute_similarity(trajectory_a, trajectory_b)

    def from_name(name: str) -> TrajectorySimilarityCalculator:
        if name == DTW_NAME:
            return Calculator.DTW
        elif name == SDTW_NAME:
            return Calculator.SDTW
        elif name == HAUSDORFF_NAME:
            return Calculator.HAUSDORFF
        else:
            raise RuntimeError("Unknown calculator: {}".format(name))
