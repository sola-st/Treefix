# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""A DistributedValues object with two tensors of [1, 2, 2] on each replica gathers along 0th dim to a tensor of [2, 2, 2]."""
single_value = constant_op.constant([[[1, 2], [1, 2]]])
axis = 0
self._gather_same_shape_and_verify(single_value, axis, pure_eager, strategy)
