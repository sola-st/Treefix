# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Initializes the object.

    Args:
      num_packs: a non-negative integer. The number of packs to split values
        into. If zero, no packing will be done.

    Raises:
      ValueError: if `num_packs` is negative.
    """
if num_packs < 0:
    raise ValueError(
        "NCCL all-reduce requires num_packs >= 0, but {} is specified".format(
            num_packs))
super(NcclAllReduce, self).__init__(
    all_reduce_alg="nccl", num_packs=num_packs)
