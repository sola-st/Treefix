# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
with backprop.GradientTape(persistent=True) as tape:
    k = constant_op.constant(1.0)
    k2 = constant_op.constant(2.0)
    v = constant_op.constant(11.0)
    v2 = constant_op.constant(22.0)
    tape.watch(v)
    tape.watch(v2)
    m = map_ops.empty_tensor_map()
    m = map_ops.tensor_map_insert(m, k, v)
    m = map_ops.tensor_map_insert(m, k2, v2)
    l1 = map_ops.tensor_map_lookup(m, k, v.dtype)
    l2 = map_ops.tensor_map_lookup(m, k2, v2.dtype)
    g = tape.gradient(l1 * l2, [v, v2])
    self.assertAllClose(g, [v2, v])
    g2 = tape.gradient(l1 * l1, v)
    self.assertAllClose(g2, 2 * v)
del tape
