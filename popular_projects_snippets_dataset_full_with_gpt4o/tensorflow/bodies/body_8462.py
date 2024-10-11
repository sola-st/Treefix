# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""A DistributedValues object with two tensors of [1, 3] on each replica gathers along 1st dim to a tensor of [1, 6]."""
single_value = constant_op.constant([[1, 2, 3]])
axis = 1
self._gather_same_shape_and_verify(single_value, axis, pure_eager, strategy)
