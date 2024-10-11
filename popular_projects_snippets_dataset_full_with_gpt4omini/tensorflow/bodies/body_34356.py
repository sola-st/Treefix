# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
with backprop.GradientTape() as tape:
    m = map_ops.empty_tensor_map()
    k = constant_op.constant(1.0)
    v = constant_op.constant(11.0)
    tape.watch(v)
    m = map_ops.tensor_map_insert(m, k, v)
    l = map_ops.tensor_map_lookup(m, k, dtypes.float32)
    l *= 5
    g = tape.gradient(l, v)
    self.assertAllEqual(g, 5)
