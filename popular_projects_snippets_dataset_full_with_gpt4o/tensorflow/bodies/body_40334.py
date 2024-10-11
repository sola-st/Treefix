# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
v1 = resource_variable_ops.ResourceVariable(1.)
self.evaluate(v1.initializer)
with backprop.GradientTape() as t:
    loss = 2 * v1
    grad = t.gradient(loss, v1)
self.assertAllEqual(self.evaluate(grad), 2.0)

with backprop.GradientTape(persistent=True) as t:
    loss = 2 * v1
    grad = t.gradient(loss, v1)
self.assertAllEqual(self.evaluate(grad), 2.0)
