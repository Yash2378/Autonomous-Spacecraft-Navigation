# tests/test_path_planning.py

from navigation import path_planning

def test_plan_path():
    start = (0, 0)
    goal = (10, 10)
    obstacles = [(3, 3), (5, 5), (7, 7)]
    
    path = path_planning.plan_path(start, goal, obstacles)
    assert path[0] == start
    assert path[-1] == goal
    assert len(path) > 1  # Ensure that a path is actually planned
