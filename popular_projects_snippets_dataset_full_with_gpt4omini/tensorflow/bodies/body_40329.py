# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = [
    resource_variable_ops.ResourceVariable(2.),
    resource_variable_ops.ResourceVariable(3.),
    resource_variable_ops.ResourceVariable(5.)
]
with backprop.GradientTape() as t:
    f = max(x)
grad = t.gradient(f, x)
self.assertAllEqual(self.evaluate(f), 5.)
self.assertAllEqual(self.evaluate(grad), [None, None, 1.0])
