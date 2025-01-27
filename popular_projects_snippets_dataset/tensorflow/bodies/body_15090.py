# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
x = ragged_factory_ops.constant([[1.0, 2.0], [3.0]])

with backprop.GradientTape() as t:
    t.watch(x)
    y = ragged_factory_ops.constant([[2.0, 4.0], [6.0]])
self.assertIsNone(t.gradient(y, x))
