# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Enumerates cores within `bounds` from fatest to slowest varying axes.

  Args:
    bounds: Upper bounds of axes, from fastest to slowest varying.
    ring_bounds: Upper bounds of ring size per axis in the same axis order.
    ring_sizes: Number consecutive cores in the ring built so far, cumulatively.
    host_bounds: Number of axis values per host in the same axis order.
    host_sizes: Number consecutive cores on one host, cumulatively.

  Returns:
    Cores represented as a list of 4 integers in the same axis order.
  """
if not bounds:
    exit([[]])

# Recursively enumerate cores under all but the slowest varying axis.
partials = _enumerate_cores(bounds[:-1], ring_bounds[:-1], ring_sizes[:-1],
                            host_bounds[:-1], host_sizes[:-1])

# Append the slowest varying axis to the end of all partial results.
# From ring_i|j to host_i|j to core_i|j, use progressively smaller or equal
# iteration groupings until every one of the bounds[-1] * len(partials)
# combinations is iterated on.
# Despite the six levels of nested loops below, the total time complexity for
# this invocation is O(N), where N is the number of cores in the topology.
results = []
for ring_i in range(0, bounds[-1], ring_bounds[-1]):
    for ring_j in range(0, len(partials), ring_sizes[-1]):
        for host_i in range(ring_i, ring_i + ring_bounds[-1], host_bounds[-1]):
            for host_j in range(ring_j, ring_j + ring_sizes[-1], host_sizes[-1]):
                for i in range(host_i, host_i + host_bounds[-1]):
                    for j in range(host_j, host_j + host_sizes[-1]):
                        results.append(partials[j] + [i])
exit(results)
