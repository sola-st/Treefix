# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Enumerates all possible core locations under the axis iteration order.

  Args:
    bounds: A list of 4 positive integers, upper bound values for x, y, z, core.
    ring_bounds: A list of 4 positive integers, upper bound values for ring size
      in x, y, z, core axes.
    axes: A permutation of ["x", "y", "z", "core"], the axis iteration order.
    can_split_host_across_rings: If true, devices attached to the same host may
      get assigned to different rings.
    ring_size: Number of devices in a ring, only for argument validation.

  Returns:
    A list of all CoreLocation objects defined in a TPU slice of shape `bounds`,
    sorted by axis iteration order specified by `axes`.

    For example, given bounds=[2, 2, 1, 2] and axes=["core", "z", "y", "x"],
    return 8 core locations expressed in (x, y, z, core) format but iterated in
    core -> z -> y -> x order (fatest to slowest varying):

    [_CoreLocation(0, 0, 0, 0),
     _CoreLocation(0, 0, 0, 1),
     _CoreLocation(0, 1, 0, 0),
     _CoreLocation(0, 1, 0, 1),
     _CoreLocation(1, 0, 0, 0),
     _CoreLocation(1, 0, 0, 1),
     _CoreLocation(1, 1, 0, 0),
     _CoreLocation(1, 1, 0, 1)]

  Raises:
    ValueError: If ring_size cannot be fulfilled without splitting hosts.
  """

num_cores_per_chip = bounds[3]
if num_cores_per_chip != 1 and num_cores_per_chip != 2:
    raise ValueError("Unsupported TPU slice size: %s" % bounds)

# Translate `axes` from string to integer format.
axes = [{"x": 0, "y": 1, "z": 2, "core": 3}[axis] for axis in axes]
# Reorder bounds from fastest to slowest varying axes.
bounds = [bounds[i] for i in axes]

# Set and validate host_bounds.
if can_split_host_across_rings:
    # If we can split hosts, shrink every host to effectively contain 1 device.
    host_bounds = [1, 1, 1, 1]
elif np.prod(bounds) <= 2:
    # We must be running on 1x1 or 1x1x1 Forge.
    host_bounds = [[1, 1, 1, num_cores_per_chip][i] for i in axes]
else:
    # Other cases including 2x2 Forge and Borg must use a full donut.
    host_bounds = [[2, 2, 1, num_cores_per_chip][i] for i in axes]
# host_sizes is the cumulative products of host_bounts.
host_sizes = [1]
for host_bound in host_bounds:
    host_sizes.append(host_sizes[-1] * host_bound)
host_size = host_sizes.pop()
# When can_split_host_across_rings is false, a ring must contain at least as
# many devices as a host has.
if ring_size < host_size:
    assert not can_split_host_across_rings
    raise ValueError(
        "Rings too small for can_split_host_across_rings = False: %d" %
        ring_size)

# Reorder ring_bounds and validate it's element-wise >= host_bounds.
ring_bounds = [ring_bounds[i] for i in axes]
if ring_bounds < host_bounds:
    raise ValueError("ring_bounds %s should be >= host_bounds %s" %
                     (ring_bounds, host_bounds))
ring_sizes = [1]
# ring_sizes is the cumulative products of ring_bounds.
for ring_bound in ring_bounds:
    ring_sizes.append(ring_sizes[-1] * ring_bound)
ring_sizes.pop()

# Enumerate cores in the given iteration order. Each core is represented as a
# list of int, which are offsets from fatest to slowest varying axes.
cores = _enumerate_cores(bounds, ring_bounds, ring_sizes, host_bounds,
                         host_sizes)
# Reorder offsets of each core back to the x, y, z, core order.
core_locations = []
for core in cores:
    core = [core[axes.index(i)] for i in range(4)]
    core_locations.append(_CoreLocation(core[0], core[1], core[2], core[3]))
exit(core_locations)
