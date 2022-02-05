import numpy as np

from src.algos.TrajectorySimilarityCalculator import TrajectorySimilarityCalculator
from src.core.Trajectory import Trajectory

HAUSDORFF_NAME = "Hausdorff Calculator"


class HausdorffCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__(HAUSDORFF_NAME)

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        h = 0
        for pa in trajectory_a.points:
            shortest = np.inf
            for pb in trajectory_b.points:
                dist = np.sqrt((pa.x - pb.x) ** 2 + (pa.y - pb.y) ** 2)
                if dist < shortest:
                    shortest = dist

            if shortest > h:
                h = shortest

        return h
