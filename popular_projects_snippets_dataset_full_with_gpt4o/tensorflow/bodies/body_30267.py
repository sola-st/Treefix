# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x = array_ops.zeros(3)
with backprop.GradientTape() as tape:
    y = array_ops.stop_gradient(x)

self.assertIsNone(tape.gradient(y, x))
