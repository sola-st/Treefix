# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=False) as tape:
    x = resource_variable_ops.ResourceVariable(1.0)
    tape.watch(x)
tape.gradient(x, x)
self.assertEqual((x,), tape.watched_variables())
