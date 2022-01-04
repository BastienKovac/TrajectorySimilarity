from src.algos.TrajectorySimilarityCalculator import TrajectorySimilarityCalculator
from src.core.Trajectory import Trajectory
from fastdtw import fastdtw

DTW_NAME = "DTW Calculator"


class DTWCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__(DTW_NAME)

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        return fastdtw([[p.x, p.y] for p in trajectory_a.points], [[p.x, p.y] for p in trajectory_b.points])
