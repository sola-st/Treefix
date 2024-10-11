# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x1 = resource_variable_ops.ResourceVariable(2.0, trainable=False)
x2 = resource_variable_ops.ResourceVariable(2.0, trainable=False)

with backprop.GradientTape() as tape1:
    with backprop.GradientTape() as tape2:
        tape1.watch(x1)
        tape2.watch([x1, x2])
        y = x1**3
        z = x2**2
        dy, dz = tape2.gradient([y, z], [x1, x2])
    d2y, d2z = tape1.gradient([dy, dz], [x1, x2])

self.evaluate([x1.initializer, x2.initializer])
self.assertEqual(self.evaluate(d2y), 12.0)
self.assertIsNone(d2z)
