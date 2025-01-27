# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
with backprop.GradientTape(persistent=True) as tape:
    m = map_ops.empty_tensor_map()
    k = constant_op.constant("key")
    k2 = constant_op.constant("key2")
    v = constant_op.constant(2.0)
    v2 = constant_op.constant(22.0)
    tape.watch(v)
    tape.watch(v2)
    m = map_ops.tensor_map_insert(m, k, v)
    m = map_ops.tensor_map_insert(m, k2, v2)
    s = map_ops.tensor_map_size(m)
    self.assertAllEqual(s, 2)
    # Test lookup and gradient.
    l = map_ops.tensor_map_lookup(m, k, v.dtype)
    self.assertAllClose(l, v)
    self.assertAllClose(tape.gradient(l * 5, v), 5)
    # Test replace and gradient.
    m = map_ops.tensor_map_insert(m, k, v2)
    l2 = map_ops.tensor_map_lookup(m, k, v2.dtype)
    self.assertAllClose(l2, v2)
    g = tape.gradient(l2 * 6, v2)
    self.assertAllEqual(g, 6)
    # Test erase, has key, and gradient.
    m = map_ops.tensor_map_erase(m, k, v2.dtype)
    s = map_ops.tensor_map_size(m)
    self.assertAllEqual(s, 1)
    h = map_ops.tensor_map_has_key(m, k)
    self.assertAllEqual(h, False)
    l = map_ops.tensor_map_lookup(m, k2, v2.dtype)
    g2 = tape.gradient(l * 6, v2)
    self.assertAllEqual(g2, 6)
del tape
