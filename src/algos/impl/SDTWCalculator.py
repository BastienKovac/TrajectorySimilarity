import numpy as np

from src.algos.TrajectorySimilarityCalculator import TrajectorySimilarityCalculator
from src.core.Trajectory import Trajectory, Point

SDTW_NAME = "SDTW Calculator"


class SDTWCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super().__init__(SDTW_NAME)

    def needs_timed_trajectory(self) -> bool:
        return True

    def _mid_point(self, a: Point, b: Point) -> Point:
        return Point((a.x + b.x) / 2, (a.y + b.y) / 2)

    def _compute_point_segment_distance(self, a: Point, mid_1: Point, mid_2: Point) -> float:
        r = (mid_2.x - mid_1.x) * (a.x - mid_1.x) + (mid_2.y - mid_1.y) * (a.y - mid_1.y)
        lseg = np.sqrt((mid_2.x - mid_1.x) ** 2 + (mid_2.y - mid_1.y) ** 2)

        dx = (mid_1.x + (mid_2.x - mid_1.x) * (r / lseg))
        dy = (mid_1.y + (mid_2.y - mid_1.y) * (r / lseg))

        if r <= 0:
            dist = np.sqrt((a.x - mid_1.x) ** 2 + (a.y - mid_1.y) ** 2)
        elif r >= lseg:
            dist = np.sqrt((a.x - mid_2.x) ** 2 + (a.y - mid_2.y) ** 2)
        else:
            dist = np.sqrt((a.x - dx) ** 2 + (mid_1.y - dy) ** 2)

        return dist

    def _compute_temporal_distance(self, a: list, b: list, i: int, j: int) -> float:
        if a[i].time > b[j].time:
            before = b[j]
            after = a[i]

            previous_b = after if i == 0 else a[i - 1]  # Point before the later one
        else:
            before = a[i]
            after = b[j]

            previous_b = after if j == 0 else b[j - 1]  # Point before the later one

        delta = before.time - after.time

        vx = (after.x - previous_b.x) / delta if delta != 0 else 0
        vy = (after.y - previous_b.y) / delta if delta != 0 else 0

        xb = previous_b.x + vx * (after.time + delta - previous_b.time)
        yb = previous_b.y + vy * (after.time + delta - previous_b.time)

        return np.sqrt((before.x - xb) ** 2 + (before.y - yb) ** 2)

    def _compute_segment_segment_distance(self, a: list, b: list, i: int, j: int, ps_dist: np.ndarray,
                                          t_dist: np.ndarray) -> float:
        return 0

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        super().compute_similarity(trajectory_a, trajectory_b)

        a, b = trajectory_a.points, trajectory_b.points
        n, m = len(a), len(b)

        ps_dist = np.zeros((n, m))
        for i in range(0, n):
            for j in range(0, m):
                ab_dist = self._compute_point_segment_distance(a[i],
                                                               b[j] if j == 0 else self._mid_point(b[j - 1], b[j]),
                                                               b[j] if j == m - 1 else self._mid_point(b[j], b[j + 1]))

                ba_dist = self._compute_point_segment_distance(b[j],
                                                               a[i] if i == 0 else self._mid_point(a[i - 1], a[i]),
                                                               a[i] if i == n - 1 else self._mid_point(a[i], a[i + 1]))
                ps_dist[i, j] = ab_dist + ba_dist

        t_dist = np.zeros((n, m))
        for i in range(0, n):
            for j in range(0, m):
                t_dist[i, j] = self._compute_temporal_distance(a, b, i, j)

        s_dist = np.zeros((n - 1, m - 1))
        for i in range(0, n - 1):
            for j in range(0, m - 1):
                s_dist[i, j] = self._compute_segment_segment_distance(a, b, i, j, ps_dist, t_dist)

        sdtw_matrix = np.ones((n, m)) * np.inf
        sdtw_matrix[0, 0] = 0

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                sdtw_matrix[i, j] = s_dist[i, j] + min(sdtw_matrix[i - 1, j - 1],
                                                       sdtw_matrix[i - 1, j], sdtw_matrix[i, j - 1])

        return sdtw_matrix[n - 2, m - 2]

