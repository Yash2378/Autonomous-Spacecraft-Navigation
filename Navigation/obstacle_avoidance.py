# navigation/obstacle_avoidance.py

import numpy as np

def avoid_obstacles(path, obstacles):
    safe_path = []
    obstacles = set(obstacles)
    for point in path:
        if point in obstacles:
            # Applying a simple repulsion force to move away from the obstacle
            safe_point = (point[0] + np.random.choice([-1, 1]), point[1] + np.random.choice([-1, 1]))
            while safe_point in obstacles:
                safe_point = (point[0] + np.random.choice([-1, 1]), point[1] + np.random.choice([-1, 1]))
            safe_path.append(safe_point)
        else:
            safe_path.append(point)
    return safe_path
