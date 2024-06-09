# tests/test_obstacle_avoidance.py

from navigation import obstacle_avoidance

def test_avoid_obstacles():
    path = [(0, 0), (10, 10)]
    obstacles = [(5, 5)]
    
    safe_path = obstacle_avoidance.avoid_obstacles(path, obstacles)
    assert all(point not in obstacles for point in safe_path)
