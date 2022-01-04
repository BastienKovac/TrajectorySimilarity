from src.algos.TrajectorySimilarityCalculator import TrajectorySimilarityCalculator
from src.core.Trajectory import Trajectory

import numpy as np

DTW_NAME = "DTW Calculator"


class DTWCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__(DTW_NAME)

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        a, b = trajectory_a.points, trajectory_b.points
        n, m = len(a), len(b)

        dtw_matrix = np.ones((n + 1, m + 1)) * np.inf
        dtw_matrix[0, 0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Use Euclidian distance
                cost = np.sqrt((a[i - 1].x - b[j - 1].x) ** 2 + (a[i - 1].y - b[j - 1].y) ** 2)
                last_min = np.min([dtw_matrix[i - 1, j], dtw_matrix[i, j - 1], dtw_matrix[i - 1, j - 1]])
                dtw_matrix[i, j] = cost + last_min

        return dtw_matrix[n, m]
