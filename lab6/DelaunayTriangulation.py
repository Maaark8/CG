import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

def generate_delaunay(points):
    delaunay = Delaunay(points)

    # Plot Delaunay triangulation
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.triplot(points[:, 0], points[:, 1], delaunay.simplices, 'b-', label='Delaunay Triangles')

    # Plot the input points
    ax.plot(points[:, 0], points[:, 1], 'ro', label='Input Points')

    # Add labels and formatting
    ax.set_xlim(min(points[:, 0]) - 1, max(points[:, 0]) + 1)
    ax.set_ylim(min(points[:, 1]) - 1, max(points[:, 1]) + 1)
    ax.set_title("Delaunay Triangulation", fontsize=16)
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)

    plt.show()

if __name__ == "__main__":
    points = [(3, -5), (-6, 6), (6, -4), (5, -5), (9, 10)]
    generate_delaunay(np.array(points))