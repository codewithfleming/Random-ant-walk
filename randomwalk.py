from random import choice

class RandomWalk:
    """
    A class to generate random walks in 2D space.

    Attributes:
        total_steps (int): The total number of steps in the walk.
        x_points (list[int]): List of x-coordinates for the walk.
        y_points (list[int]): List of y-coordinates for the walk.
    """

    def __init__(self, total_steps=0):
        """
        Initializes a random walk with an optional step count.

        Args:
            total_steps (int, optional): The total steps for the walk. Defaults to 0.
        """
        self.total_steps = total_steps
        self.x_points = [0]
        self.y_points = [0]

    def fill_walk(self):
        """ Fills the walk with random points until the total step count is reached.
        Prompts the user to enter a step count if not provided."""
        while True:
            try:
                steps = int(input("How many steps do you want your ant to move in total? "))
                break
            except ValueError:
                print("Please enter your steps in figures")

        self.total_steps = steps

        while len(self.x_points) < self.total_steps:
            x_direction = choice([1, -1])
            x_distance = choice(range(1, 4))
            x_steps = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice(range(1, 4))
            y_steps = y_direction * y_distance

            if x_steps == 0 and y_steps == 0:
                continue

            # compute new point
            self.x_points.append(self.x_points[-1] + x_steps)
            self.y_points.append(self.y_points[-1] + y_steps)
