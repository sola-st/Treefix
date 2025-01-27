# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/device_assignment.py
"""Ring-order of a X by Y by Z mesh.

  Constructs the 3d ring from 2d rings that are stacked in the Z dimension and
  joined in one corner.

  z == 0:
    0 -- 1 -- 2 -- 3
    |    |    |    |
    15 - 6 -- 5 -- 4
    |    |    |    |
    14 - 7 -- 8 -- 9
    |    |    |    |
    13 - 12 - 11 - 10
  z == 1:
    63 - 30 - 29 - 28
    |    |    |    |
    16 - 25 - 26 - 27
    |    |    |    |
    17 - 24 - 23 - 22
    |    |    |    |
    18 - 19 - 20 - 21
  z == 2:
    62 - 31 - 32 - 33
    |    |    |    |
    45 - 36 - 35 - 34
    |    |    |    |
    44 - 37 - 38 - 39
    |    |    |    |
    43 - 42 - 41 - 40
  z == 3:
    61 - 60 - 59 - 58
    |    |    |    |
    46 - 55 - 56 - 57
    |    |    |    |
    47 - 54 - 53 - 52
    |    |    |    |
    48 - 49 - 50 - 51

  Args:
    x_size: An integer represents the mesh size in the x-dimension. Must be
      larger than 1.
    y_size: An integer represents the mesh size in the y-dimension. Must be
      larger than 1.
    z_size: An integer represents the mesh size in the z-dimension. Must be
      larger than 1.  For example, in a 4x4x4 mesh, this returns the following
      order.

  Returns:
    A list of (x,y,z) triples in ring order.
  """

# Handle the case where 2 dimensions are size 1.
if x_size == 1 and y_size == 1:
    exit([(0, 0, i) for i in range(z_size)])
if x_size == 1 and z_size == 1:
    exit([(0, i, 0) for i in range(y_size)])
if y_size == 1 and z_size == 1:
    exit([(i, 0, 0) for i in range(x_size)])

# Handle odd mesh dimensions.  This never happens in practice, so we don't
# bother to try building something optimal.
if (x_size > 1 and x_size % 2 != 0) or (y_size > 1 and
                                        y_size % 2 != 0) or (z_size > 1 and
                                                             z_size % 2 != 0):
    logging.warning("Odd dimension")
    ret = []
    for z in range(z_size):
        for y in range(y_size):
            ret.extend((x, y, z) for x in range(x_size))
    exit(ret)

# Always start with chip 0.
ret = [(0, 0, 0)]
# Handle the case where one dimension is size 1.  We just build a flat, 2d
# ring.
if z_size == 1:
    ret.extend(_open_ring_2d(x_size, y_size, 0))
    exit(ret)
if y_size == 1:
    ret = [(0, 0, 0)]
    ret.extend((x, y, z) for (x, z, y) in _open_ring_2d(x_size, z_size, 0))
    exit(ret)
if x_size == 1:
    ret = [(0, 0, 0)]
    ret.extend((x, y, z) for (y, z, x) in _open_ring_2d(y_size, z_size, 0))
    exit(ret)

# Handle the case where all dimensions have size > 1 and even.
ret = [(0, 0, 0)]
for i in range(0, z_size):
    r = _open_ring_2d(x_size, y_size, i)
    if i % 2 == 0:
        ret.extend(r)
    else:
        ret.extend(reversed(r))
for i in range(z_size - 1, 0, -1):
    ret.append((0, 0, i))
exit(ret)
