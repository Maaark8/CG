# Voronoi Diagram and Delaunay Triangulation

Python implementations for generating and visualizing **Voronoi Diagrams** and **Delaunay Triangulations** using `scipy` and `matplotlib`.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.7 or later
- `numpy`
- `matplotlib`
- `scipy`

You can install the required Python packages using `pip`:

```bash
pip install numpy matplotlib scipy
```

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/voronoi-delaunay.git
    ```

2. Navigate to the project directory:

    ```bash
    cd voronoi-delaunay
    ```

## Usage

### Voronoi Diagram

To generate and visualize a Voronoi diagram:

1. Open the terminal and run:

    ```bash
    python Voronoi.py
    ```

2. This will generate a Voronoi diagram for a set of points and display it using `matplotlib`.

You can modify the script to provide custom points by editing the `points` variable in `voronoi_diagram.py`.

### Delaunay Triangulation

To generate and visualize a Delaunay triangulation:

1. Open the terminal and run:

    ```bash
    python DelaunayTriangulation.py
    ```

2. This will generate a Delaunay triangulation for a set of points and display it using `matplotlib`.

Similar to the Voronoi script, you can modify the `points` variable in `delaunay_triangulation.py` to use custom data.
