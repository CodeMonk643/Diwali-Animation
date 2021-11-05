import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
 
# Fixing random state for reproducibility
np.random.seed(9740320)
 
 
class drops:
    def __init__(self, msg, n_drops=50):
 
        self.msg = msg
        self.ndrops = n_drops
        self.COLORS = matplotlib.cm.rainbow(np.linspace(0, 1, self.ndrops))
        # Create new Figure and an Axes which fills it and set background black
        self.fig = plt.figure(figsize=(7, 7))
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon=False)
        self.ax.set_xlim(0, 1)
        self.ax.set_xticks([])
        self.ax.set_ylim(0, 1)
        self.ax.set_yticks([])
        self.fig.patch.set_facecolor('black')
        # Add text
        pos = 1 - (len(self.msg)+6)/100
        self.ax.text(pos, 0.10, msg, color="white")
        # Add shadow
        self.ax.text(pos+0.01, 0.095, msg, color="grey", alpha=0.5)
 
        # Initialize the drops with random positions and with
        # random growth rates.
        self.position = np.random.uniform(0, 1, (self.ndrops, 2))
        self.growth = np.random.uniform(50, 200, self.ndrops)
        self.colors = self.COLORS.copy()
        self.sizes = np.zeros((self.ndrops))
 
        # Construct the scatter which we will update during animation
        # as the drops develop.
        self.scat = self.ax.scatter(self.position[:, 0], self.position[:, 1],
                                    s=self.sizes, lw=0.5, c=self.colors, edgecolors=self.colors,
                                    facecolors=self.colors)
 
    def __call__(self, frame_number):
        # Get an index which we can use to re-spawn the oldest drop.
        current_index = frame_number % self.ndrops
 
        # Make all colors more transparent as time progresses.
        self.colors[:, 3] -= 1.0/self.ndrops
        self.colors[:, 3] = np.clip(self.colors[:, 3], 0, 1)
 
        # Make all circles bigger.
        self.sizes += self.growth
 
        # Pick a new position for oldest drop, resetting its size,
        # color and growth factor.
        self.position[current_index] = np.random.uniform(0, 1, 2)
        self.sizes[current_index] = 5
        self.colors[current_index] = self.COLORS[current_index]
        self.growth[current_index] = np.random.uniform(50, 200)
 
        # Update the scatter collection, with the new colors, sizes and positions.
        self.scat.set_color(self.colors)
        self.scat.set_edgecolors(self.colors)
        self.scat.set_sizes(self.sizes)
        self.scat.set_offsets(self.position)
 
    def show(self):
        # Construct the animation, using the update function as the animation director.
        animation = FuncAnimation(self.fig, self.__call__, interval=10)
        plt.show()
 
 
if __name__ == "__main__":
    dd = drops("Happy Diwali").show()
