# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
v1 = resource_variable_ops.ResourceVariable(1.)
self.evaluate(v1.initializer)
with backprop.GradientTape() as t:
    with self.assertRaises(ValueError):
        with t:
            pass
