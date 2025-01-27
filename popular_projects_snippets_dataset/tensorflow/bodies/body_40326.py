# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as t:
    x = resource_variable_ops.ResourceVariable(1.0)
    with t.stop_recording():
        y = x * x
self.assertEqual(t.gradient(y, x), None)
