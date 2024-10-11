# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as g:
    x = variables.Variable([3.0])
    y = variables.Variable([2.0])
grad = g.gradient(x, y)
self.assertAllEqual(grad, None)
