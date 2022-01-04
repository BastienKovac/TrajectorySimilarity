from src.algos.TrajectorySimilarityCalculator import TrajectorySimilarityCalculator
from src.core.Trajectory import Trajectory

HAUSDORFF_NAME = "Hausdorff Calculator"


class HausdorffCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__(HAUSDORFF_NAME)

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError
