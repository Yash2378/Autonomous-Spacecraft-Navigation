from navigation import path_planning, obstacle_avoidance, route_adjustment, simulation

def main():
    # Define the starting point, goal, and obstacles
    start = (0, 0)
    goal = (10, 10)
    obstacles = [(3, 3), (5, 5), (7, 7), (5, 3), (3, 5)]

    # Plan the initial path using the path planning module
    path = path_planning.plan_path(start, goal, obstacles)
    print(f"Planned Path: {path}")

    # Avoid obstacles along the planned path using the obstacle avoidance module
    safe_path = obstacle_avoidance.avoid_obstacles(path, obstacles)
    print(f"Safe Path: {safe_path}")

    # Adjust the route dynamically based on real-time data using the route adjustment module
    final_route = route_adjustment.adjust_route(safe_path, real_time_data={})
    print(f"Final Route: {final_route}")

    # Run a simulation to visualize the navigation
    simulation.run_simulation(start, goal, obstacles, final_route)

if __name__ == "__main__":
    main()
