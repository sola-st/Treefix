# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
m = map_ops.empty_tensor_map()
k = constant_op.constant("key")
v = constant_op.constant("value")
k2 = constant_op.constant(1.0)
v2 = constant_op.constant(2.0)
# Test insert and lookup on string key-value pair.
m = map_ops.tensor_map_insert(m, k, v)
m = map_ops.tensor_map_insert(m, k2, v2)
l = map_ops.tensor_map_lookup(m, k, v.dtype)
self.assertAllEqual(l, v)
# Test lookup on float key-value pair.
l2 = map_ops.tensor_map_lookup(m, k2, v2.dtype)
self.assertAllClose(l2, v2)
# Test erase and has key.
self.assertAllEqual(map_ops.tensor_map_has_key(m, k), True)
m = map_ops.tensor_map_erase(m, k, v.dtype)
self.assertAllEqual(map_ops.tensor_map_has_key(m, k), False)
self.assertAllEqual(map_ops.tensor_map_has_key(m, k2), True)
