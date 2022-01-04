from src.algos.TrajectorySimilarityCalculator import TrajectorySimilarityCalculator
from typing import List, Dict
from src.core.Trajectory import Trajectory

from src.algos.impl.DTWCalculator import DTWCalculator, DTW_NAME
from src.algos.impl.SDTWCalculator import SDTWCalculator, SDTW_NAME
from src.algos.impl.HausdorffCalculator import HausdorffCalculator, HAUSDORFF_NAME

from abc import ABC

from enum import Enum


class CalculatorContext:

    def __init__(self, calculator: TrajectorySimilarityCalculator) -> None:
        self._calculator = calculator

    @property
    def calculator(self) -> TrajectorySimilarityCalculator:
        return self._calculator

    @calculator.setter
    def calculator(self, calculator: TrajectorySimilarityCalculator) -> None:
        self._calculator = calculator

    def compute_similarity(self, query: Trajectory, references: List[Trajectory]) -> Dict[Trajectory, float]:
        """
        Compute the similarity between the trajectory query and all reference trajectories.
        Returns a dict containing, for each reference trajectory, the computed similarity score
        :param query: The query trajectory
        :param references: The reference trajectories
        """
        return {reference: self.calculator.compute_similarity(query, reference) for reference in references}


class _FinalMeta(type(Enum), type(ABC)):
    pass


class Calculator(TrajectorySimilarityCalculator, Enum, metaclass=_FinalMeta):
    DTW = DTWCalculator()
    SDTW = SDTWCalculator()
    HAUSDORFF = HausdorffCalculator()

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
