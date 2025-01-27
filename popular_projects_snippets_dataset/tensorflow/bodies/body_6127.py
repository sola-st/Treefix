# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Initializes the object.

    Args:
      all_reduce_alg: the all-reduce algorithm to use, currently only "nccl" or
        "hierarchical_copy" are supported.
      num_packs: a non-negative integer. The number of packs to split values
        into. If zero, no packing will be done.
    """
self._all_reduce_alg = all_reduce_alg
self._num_packs = num_packs
self._simple_cross_replica_ops = ReductionToOneDevice()
super(AllReduceCrossDeviceOps, self).__init__()
