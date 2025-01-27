# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
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
