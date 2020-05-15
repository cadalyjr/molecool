"""
molecool
A Python package for analyzing and visualizing pdb and xyz files. For MolSSI May webinar series.
"""

# Add imports here
from .functions import canvas, zen #canvas
# it's considered "bad practice" to import *, as opposed to specfic functions
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram
from .measure import calculate_angle, calculate_distance
from .atom_data import atomic_weights, atom_colors
from molecool.io import open_pdb, open_xyz, write_xyz

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
