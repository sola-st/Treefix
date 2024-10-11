# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
with backprop.GradientTape(persistent=True) as tape:
    m = map_ops.empty_tensor_map()
    k = constant_op.constant(1.0)
    k2 = constant_op.constant(2.0)
    v = constant_op.constant(11.0)
    v2 = constant_op.constant(22.0)
    tape.watch(v)
    tape.watch(v2)
    m = map_ops.tensor_map_insert(m, k, v)
    m = map_ops.tensor_map_insert(m, k2, v2)
    m = map_ops.tensor_map_erase(m, k2, v2.dtype)
    l = map_ops.tensor_map_lookup(m, k, v.dtype)
    self.assertAllClose(l, v)
    g = tape.gradient(l * 5, v)
    self.assertAllEqual(g, 5)
del tape
