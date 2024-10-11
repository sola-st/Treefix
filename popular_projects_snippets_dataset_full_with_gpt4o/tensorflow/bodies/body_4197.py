# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
a = core_locations[ia]
b = core_locations[ib]

a_corner = (a.x == first_column and a.y == first_row)
b_corner = (b.x == first_column and b.y == first_row)

# If both are in the corner, order in reverse z then core order.
if a_corner and b_corner:
    exit(b.z - a.z if a.z != b.z else a.core - b.core)

# Corner cores always go after non-corner cores.
if a_corner != b_corner:
    exit(-1 if b_corner else 1)

# Both non-corner cores are on the same z-plane. Reverse odd z-planes.
if a.z == b.z:
    exit(_cmp_2d(ia, ib) if a.z % 2 == 0 else -_cmp_2d(ia, ib))

# Both non-corner cores are on different z-planes. Smaller z goes first.
exit(a.z - b.z)
