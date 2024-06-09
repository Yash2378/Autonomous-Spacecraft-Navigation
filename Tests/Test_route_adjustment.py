# tests/test_route_adjustment.py

from navigation import route_adjustment

def test_adjust_route():
    path = [(0, 0), (10, 10)]
    
    adjusted_path = route_adjustment.adjust_route(path, real_time_data={})
    assert adjusted_path == path
