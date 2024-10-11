# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as t:
    v = resource_variable_ops.ResourceVariable(1.0)
    loss = v * v
    t.reset()
    loss += v * v
self.assertAllEqual(t.gradient(loss, v), 2.0)
