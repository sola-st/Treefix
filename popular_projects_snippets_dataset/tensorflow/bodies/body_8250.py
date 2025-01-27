# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
# We can't use Python literals because they are treated as non-distributed
# values is not allowed when aggregation is SUM. See
# `cross_device_ops.reduce_non_distributed_value`.
delta = array_ops.identity(1.)
self.assertIsInstance(v.assign(delta), core.Tensor)
self.assertIsInstance(v.assign_sub(delta), core.Tensor)
self.assertIsInstance(v.assign_add(delta), core.Tensor)
