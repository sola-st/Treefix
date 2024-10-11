# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=False) as tape:
    x = resource_variable_ops.ResourceVariable(1.0)
    tape.watch(x)
    self.assertEqual((x,), tape.watched_variables())
    tape.reset()
    z = resource_variable_ops.ResourceVariable(2.0)
    tape.watch(z)
    self.assertEqual((z,), tape.watched_variables())
tape.gradient(z, z)
self.assertEqual((z,), tape.watched_variables())
