"""
calcs.py
A Python package for analyzing and visualizing pdb and xyz files. For MolSSI May webinar series.

Contains functions related to calculations important for characterizing molecule structure.
"""
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

def calculate_distance(rA, rB):
    # This function calculates the distance between two points given as numpy arrays.
    d=(rA-rB)
    dist=np.linalg.norm(d)
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
