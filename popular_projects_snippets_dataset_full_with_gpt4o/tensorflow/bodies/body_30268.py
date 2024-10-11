# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x = RaggedTensor.from_row_splits(values=[1, 2, 3], row_splits=[0, 1, 1, 3])
with backprop.GradientTape() as tape:
    y = array_ops.stop_gradient(x)

self.assertIsNone(tape.gradient(y, x))
