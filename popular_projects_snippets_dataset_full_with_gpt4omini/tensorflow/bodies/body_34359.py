# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
# Test using same key and different value.
with backprop.GradientTape(persistent=True) as tape:
    m = map_ops.empty_tensor_map()
    k = constant_op.constant(1.0)
    v = constant_op.constant(11.0)
    v2 = constant_op.constant(22.0)
    tape.watch(v)
    tape.watch(v2)
    m = map_ops.tensor_map_insert(m, k, v)
    l = map_ops.tensor_map_lookup(m, k, v.dtype)
    self.assertAllClose(l, v)
    g = tape.gradient(l * 5, v)
    self.assertAllEqual(g, 5)
    # Replace key and lookup.
    m = map_ops.tensor_map_insert(m, k, v2)
    l2 = map_ops.tensor_map_lookup(m, k, v2.dtype)
    self.assertAllClose(l2, v2)
    g2 = tape.gradient(l2 * 6, v)
    self.assertAllClose(g2, array_ops.zeros_like(v))
    g3 = tape.gradient(l2 * 7, v2)
    self.assertAllClose(g3, 7)
del tape
