# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x1 = resource_variable_ops.ResourceVariable(1.0)
x2 = resource_variable_ops.ResourceVariable(1.0)
with backprop.GradientTape(watch_accessed_variables=False) as tape:
    tape.watch(x2)
    y = x1**2
    z = x2**3
self.assertTupleEqual(tape.watched_variables(), (x2,))
dy, dz = tape.gradient([y, z], [x1, x2])
self.evaluate([x1.initializer, x2.initializer])
self.assertIsNone(dy)
self.assertEqual(self.evaluate(dz), 3.0)
