# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
with backprop.GradientTape() as tape:
    m = map_ops.empty_tensor_map()
    k = constant_op.constant(1.0)
    k2 = constant_op.constant(2.0)
    v = constant_op.constant(11.0)
    tape.watch(v)
    m = map_ops.tensor_map_insert(m, k, v)
    l = map_ops.tensor_map_lookup(m, k, v.dtype)
    m = map_ops.tensor_map_insert(m, k2, l)
    l2 = map_ops.tensor_map_lookup(m, k2, l.dtype)
    g = tape.gradient(l2 * 5, v)
    self.assertAllEqual(g, 5)
