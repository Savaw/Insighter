# Adapted from https://stackoverflow.com/a/25941474

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Line3DCollection


def colorline_3d(
        x, y, z, cmap=plt.get_cmap('copper'), linewidth=3, alpha=1.0):
    """
    Plot a colored line with coordinates x, y, and z
    """

    colors = np.linspace(0.0, 1.0, len(x))

    segments = make_segments(x, y, z)

    lc = Line3DCollection(segments,
                          array=colors,
                          cmap=cmap,
                          linewidth=linewidth,
                          alpha=alpha)

    ax = plt.gca()
    ax.add_collection(lc)

    return lc


def make_segments(x, y, z):
    """
    Create list of line segments from x, y, z coordinates, in the correct format
    for LineCollection: an array of the form numlines x (points per line) x 3 (x, 
    y, z) array
    """

    points = np.array([x, y, z]).T.reshape(-1, 1, 3)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments
