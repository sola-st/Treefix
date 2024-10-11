# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""all_gather(..., axis=2,...) a DistributedValues with a Tensor of shape (1,2,2) on two replica returns PerReplica of tensor(s) with shape (1,2,4)."""
single_value = constant_op.constant([[[1, 2], [1, 2]]])
axis = 2
self._all_gather_same_shape_and_verify(single_value, axis, pure_eager,
                                       strategy)
