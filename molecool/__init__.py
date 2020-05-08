"""
molecool
A Python package for analyzing and visualizing pdb and xyz files. For MolSSI May webinar series.
"""

# Add imports here
from .functions import * #canvas
# it's considered "bad practice" to import *, as opposed to specfic functions
# this syntax leads to molecool.canvas
#import molecool.functions
# this syntax leads to molecool.functions.canvas

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
