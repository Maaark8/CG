import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

def generate_voronoi(points):
    vor = Voronoi(points)

    # Plot Voronoi diagram
    fig, ax = plt.subplots(figsize=(8, 8))
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue', line_width=2, point_size=15)

    # Plot the input points
    ax.plot(points[:, 0], points[:, 1], 'ro', label='Input Points')

    # Add labels and formatting
    ax.set_xlim(min(points[:, 0]) - 1, max(points[:, 0]) + 1)
    ax.set_ylim(min(points[:, 1]) - 1, max(points[:, 1]) + 1)
    ax.set_title("Voronoi Diagram", fontsize=16)
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)

    plt.show()

if __name__ == "__main__":
    points = [(3, -5), (-6, 6), (6, -4), (5, -5) ,(9, 10)]
    generate_voronoi(np.array(points))