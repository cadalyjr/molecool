"""
Functions to visualize molecules
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from .atom_data import atom_colors

def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):
    """
    Draw a picture of a molecule using matplotlib.

    Parameters
    ----------
    coordinates : np.adarray
        The coordinates of each point in an (n, 3) array.

    symbols : Array of strings
        Array of chemical symbols with length n.

    draw_bonds : Dictionary
        Dictionary of items meant to be bonded to each other in the plot.
        Default value: None i.e. no bonds are drawn.

    save_location : string
        Location for saving output. Default value: None i.e. output is not saved.

    dpi : float or integer
        DPI value for output. Default 300.

    Returns
    -------
    ax : matplotlib axes object
        The plot with the molecular/atomic information.

    Examples
    --------
    >>> import numpy as np
    >>> coordinates = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    >>> symbols = ['H', 'H']
    >>> draw_molecule(coordinates, symbols)
    <matplotlib.axes._subplots.Axes3DSubplot object at 0x1176c5a90>
    """
    #what if coordinate and symbols lists have different lengths?
    #i.e. from diff molecules
    # Draw a picture of a molecule using matplotlib.

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])

    size = np.array(plt.rcParams['lines.markersize'] ** 2)*200/(len(coordinates))

    ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], marker="o",
               edgecolors='k', facecolors=colors, alpha=1, s=size)

    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]
            atom2 = atoms[1]

            ax.plot(coordinates[[atom1,atom2], 0], coordinates[[atom1,atom2], 1],
                    coordinates[[atom1,atom2], 2], color='k')

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi, graph_min=0, graph_max=2)

    return ax

def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    # Draw a histogram of bond lengths based on a bond_list (output from build_bond_list function)


    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)

    bins = np.linspace(graph_min, graph_max)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.xlabel('Bond Length (angstrom)')
    plt.ylabel('Number of Bonds')


    ax.hist(lengths, bins=bins)

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)

    return ax
