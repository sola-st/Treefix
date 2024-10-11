# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
original = constant_op.constant([0.2, 0.3])
updates = constant_op.constant([0.4])
with backprop.GradientTape() as tape:
    tape.watch([original, updates])
    updated = gen_array_ops.tensor_strided_slice_update(
        original, [0], [1], [1], updates)
d1, d2 = tape.gradient(updated, [original, updates],
                       output_gradients=constant_op.constant([2.0, 3.0]))
self.assertAllClose([0.0, 3.0], d1)
self.assertAllClose([2.0], d2)
