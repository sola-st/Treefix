# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""A DistributedValues object with two tensors of [1, 2, 2] on each replica gathers along 1nd dimension to a tensor of [1, 4, 2]."""
single_value = constant_op.constant([[[1, 2], [1, 2]]])
axis = 1
self._gather_same_shape_and_verify(single_value, axis, pure_eager, strategy)
