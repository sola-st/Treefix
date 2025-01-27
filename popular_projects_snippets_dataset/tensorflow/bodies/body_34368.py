# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
m = map_ops.empty_tensor_map()
k = constant_op.constant([1.0, 2.0])
v = constant_op.constant([11.0, 22.0])
# Test insert and lookup.
m = map_ops.tensor_map_insert(m, k, v)
s = map_ops.tensor_map_size(m)
self.assertAllEqual(s, 1)
l = map_ops.tensor_map_lookup(m, k, v.dtype)
self.assertAllEqual(l, v)
# Test erase and has key.
m = map_ops.tensor_map_erase(m, k, v.dtype)
s = map_ops.tensor_map_size(m)
self.assertAllEqual(s, 0)
self.assertAllEqual(map_ops.tensor_map_has_key(m, k), False)
