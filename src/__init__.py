from src.core.TrajectoryParser import parse
from pathlib import Path

# Query trajectories
QUERIES_FULL = parse((Path(__file__).parent.parent / "resources/queriesFull.json").resolve())

for query in QUERIES_FULL:
    for i in range(0, len(query.points)):
        query.points[i].time = i

QUERIES_SPARSE = parse((Path(__file__).parent.parent / "resources/queriesNotFull.json").resolve())

for query in QUERIES_SPARSE:
    for i in range(0, len(query.points)):
        query.points[i].time = i

# Base trajectories
TRAJECTORY_UNTIMED = parse((Path(__file__).parent.parent / "resources/tracksWithoutTime.json").resolve())
TRAJECTORY_TIMED = parse((Path(__file__).parent.parent / "resources/tracksWithTimes.json").resolve())

# Base Image path
BASE_IMAGE_PATH = (Path(__file__).parent.parent / "resources/BaseImage.png").resolve()
