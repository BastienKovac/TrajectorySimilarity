from src.algos.TrajectorySimilarityCalculator import TrajectorySimilarityCalculator, Trajectory


class DTWCalculator(TrajectorySimilarityCalculator):

    def __init__(self):
        super(TrajectorySimilarityCalculator, self).__init__("DTW Calculator")

    def compute_similarity(self, trajectory_a: Trajectory, trajectory_b: Trajectory) -> float:
        raise NotImplementedError
