# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
m = map_ops.empty_tensor_map()
k = constant_op.constant(1.0)
k2 = constant_op.constant(2.0)
v = constant_op.constant(2.0)
m = map_ops.tensor_map_insert(m, k, v)
# Check has key.
b = map_ops.tensor_map_has_key(m, k)
b2 = map_ops.tensor_map_has_key(m, k2)
self.assertAllEqual(b, True)
self.assertAllEqual(b2, False)
