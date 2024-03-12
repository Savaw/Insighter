import numpy as np
import matplotlib.pyplot as plt
from Lorenz.colored_plot import colorline_3d


def lorenz_step(X, B):
    x, y, z = X
    sigma, rho, beta = B

    d_x = sigma * (y - x)
    d_y = x * (rho - z) - y
    d_z = x * y - beta * z

    return np.array([d_x, d_y, d_z])


def plot_lorenz(X, B, d_t=0.01, steps=1000):
    """
    X: float np array of shape (1, 3)
        initial points
    B: float np array of shape (1, 3)
        parameters sigma, rho, beta

    d_t: float
        derivative time step
    steps: int
        total steps
    """

    d_t = 0.01
    steps = 10000

    all_X = np.array([X])
    all_X.reshape(1, 3)

    # Calculate states for #steps
    for _ in range(steps):
        d_X = lorenz_step(X, B)

        X += d_X * d_t

        all_X = np.append(all_X, X.reshape(1, 3), axis=0)

    # Plot
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Lorenz system for sigma = {round(B[0], 2)}, rho = {
                 round(B[1], 2)}, beta = {round(B[2], 2)}\n")

    min_value = all_X.min(axis=0)
    max_value = all_X.max(axis=0)
    ax.set_xlim(min_value[0], max_value[0])
    ax.set_ylim(min_value[1], max_value[1])
    ax.set_zlim(min_value[2], max_value[2])

    lc = colorline_3d(*all_X.T, cmap=plt.get_cmap('bwr'), linewidth=0.5)

    ax.add_collection(lc)

    plt.show()


if __name__ == "__main__":
    X = np.array([0, 1, 1.05], dtype=np.float64)
    B = np.array([10, 28, 8/3], dtype=np.float64)
    plot_lorenz(X, B)
