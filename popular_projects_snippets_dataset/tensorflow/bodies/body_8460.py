# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""A DistributedValues object with two tensors of shape [3] on each replica gathers to a tensor of [6]."""
single_value = constant_op.constant([1, 2, 3])
axis = 0
self._gather_same_shape_and_verify(single_value, axis, pure_eager, strategy)
