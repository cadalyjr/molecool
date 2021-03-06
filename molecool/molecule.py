"""
Functions associated with a molecule
"""

from .measure import calculate_distance

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    if min_bond < 0:
        raise ValueError(F"Current min_bond is {min_bond}. Minimum bond length must be greater than or equal to zero.")
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds
