from src.algos.TrajectorySimilarityCalculator import TrajectorySimilarityCalculator
from typing import List, Dict
from src.core.Trajectory import Trajectory


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
