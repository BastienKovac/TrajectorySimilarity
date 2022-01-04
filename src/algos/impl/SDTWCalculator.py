from src.algos.TrajectorySimilarityCalculator import TrajectorySimilarityCalculator
from src.core.Trajectory import Trajectory

SDTW_NAME = "SDTW Calculator"


class SDTWCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__(SDTW_NAME)

    def needs_timed_trajectory(self) -> bool:
        return True

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError
