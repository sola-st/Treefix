# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
v0 = resource_variable_ops.ResourceVariable(1.0)
with backprop.GradientTape() as t:
    y = v0.read_value()
self.assertEqual(t.gradient(y, v0).numpy(), 1.0)
