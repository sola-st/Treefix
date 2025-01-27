# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
m = map_ops.empty_tensor_map()
k = constant_op.constant(1.0)
k2 = constant_op.constant(2.0)
v = constant_op.constant(2.0)
m = map_ops.tensor_map_insert(m, k, v)

default_value = array_ops.zeros_like(v)
l = control_flow_ops.cond(
    map_ops.tensor_map_has_key(m, k),
    lambda: map_ops.tensor_map_lookup(m, k, dtypes.float32),
    lambda: default_value)
l2 = control_flow_ops.cond(
    map_ops.tensor_map_has_key(m, k2),
    lambda: map_ops.tensor_map_lookup(m, k, dtypes.float32),
    lambda: default_value)
self.assertAllClose(l, v)
self.assertAllClose(l2, default_value)
