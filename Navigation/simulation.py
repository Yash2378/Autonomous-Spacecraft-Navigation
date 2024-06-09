# navigation/simulation.py

import matplotlib.pyplot as plt

def run_simulation(start, goal, obstacles, path):
    fig, ax = plt.subplots()
    ax.plot(*zip(*path), marker='o', label='Path')
    ax.plot(start[0], start[1], 'go', label='Start')
    ax.plot(goal[0], goal[1], 'ro', label='Goal')
    for obs in obstacles:
        ax.plot(obs[0], obs[1], 'ks', label='Obstacle' if obs == obstacles[0] else "")
    ax.legend()
    ax.grid(True)
    plt.show()
