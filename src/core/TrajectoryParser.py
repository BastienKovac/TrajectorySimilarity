from src.core.Trajectory import Trajectory
from typing import List
from pathlib import Path

from src.core.Point import Point
from src.core.Trajectory import Trajectory

import json


def parse(file_path: Path) -> List[Trajectory]:
    with open(file_path) as f:
        data = json.load(f)

    trajectories = []

    for track in data:
        if "track" in track:
            trajectory = track["track"]
        else:
            trajectory = track

        points = []
        for p in trajectory:
            if "time" in p:
                point = Point(p["x"], p["y"], p["time"])
            else:
                point = Point(p["x"], p["y"])

            points.append(point)

        trajectories.append(Trajectory(points))

    return trajectories
