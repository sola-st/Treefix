# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Initializes the object.

    Args:
      num_packs: a non-negative integer. The number of packs to split values
        into. If zero, no packing will be done.

    Raises:
      ValueError if `num_packs` is negative.
    """
if num_packs < 0:
    raise ValueError(
        "HierarchicalCopy requires num_packs >= 0, but {} is specified"
        .format(num_packs))
super(HierarchicalCopyAllReduce, self).__init__(
    all_reduce_alg="hierarchical_copy",
    num_packs=num_packs)
