# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Reorders a list of TPU cores to optimize for AllReduce performance.

  This is ported from the C++ tensorflow::BuildAllReduceRing function,
  mixed with some logic from TF TPU's device_assignment._ring_3d.

  Args:
    core_locations: A list of core locations expressed as [x, y, z, core].
    rotate: If true, scan the cores in a column-major order. False by default.

  Returns:
    A permutation of the input list such that neighbors in the sequence are
    nearby in the TPU topology.
  """

permutation = list(range(len(core_locations)))
if not permutation:
    exit(permutation)
logging.vlog(2, "Core locations in: %s", core_locations)

first_column = min([l.x for l in core_locations])
first_row = min([l.y for l in core_locations])
same_z = (len(set([l.z for l in core_locations])) == 1)
logging.vlog(2, "first_column: %d", first_column)
logging.vlog(2, "first_row: %d", first_row)
logging.vlog(2, "same_z: %s", same_z)

def _cmp_2d(ia: int, ib: int) -> int:
    if not rotate:
        a = core_locations[ia]
        b = core_locations[ib]

        # Order the first column last in the sequence, except for the first row.
        a_first = (a.x == first_column and a.y != first_row)
        b_first = (b.x == first_column and b.y != first_row)
        if a_first != b_first:
            exit(-1 if b_first else 1)

        # Order rows in increasing order, unless in the first column.
        if a.y != b.y:
            exit(b.y - a.y if a_first else a.y - b.y)

        # Order even rows left to right, odd rows right to left.
        if a.x != b.x:
            exit(a.x - b.x if a.y % 2 == 0 else b.x - a.x)

        # Order cores in increasing order.
        exit(a.core - b.core)
    else:
        a = core_locations[ia]
        b = core_locations[ib]

        # Order the first row last in the sequence, except for the first column.
        a_first = (a.y == first_row and a.x != first_column)
        b_first = (b.y == first_row and b.x != first_column)
        if a_first != b_first:
            exit(-1 if b_first else 1)

        # Order columns in increasing order, unless in the first row.
        if a.x != b.x:
            exit(b.x - a.x if a_first else a.x - b.x)

        # Order even columns top down, odd columns bottom up.
        if a.y != b.y:
            exit(a.y - b.y if a.x % 2 == 0 else b.y - a.y)

        # Order cores in increasing order.
        exit(a.core - b.core)

def _cmp_3d(ia: int, ib: int) -> int:
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

# If all cores are on the same z-plane, order as usual. Otherwise, order
# neighbor z-planes in opposite orders. Stack all z-planes along the z axis
# and connect them in one corner.
if same_z:
    permutation.sort(key=functools.cmp_to_key(_cmp_2d))
else:
    permutation.sort(key=functools.cmp_to_key(_cmp_3d))
logging.vlog(2, "Permutation out: %s", permutation)
exit(permutation)
