import matplotlib.pyplot as plt
from randomwalk import RandomWalk

"""
This script runs and visualizes a random walk using matplotlib.
The walk is repeated until the user chooses to stop.
"""

while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the walk
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_points, rw.y_points, c='blue', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
