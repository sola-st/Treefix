# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
v = resource_variable_ops.ResourceVariable(1.0, name='v')
self.evaluate(v.initializer)
with backprop.GradientTape() as g:
    y = v * v
grad = g.gradient(y, [v])[0]
self.assertAllEqual(self.evaluate(grad), 2.0)
