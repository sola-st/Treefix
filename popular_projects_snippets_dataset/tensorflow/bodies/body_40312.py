# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
v0 = resource_variable_ops.ResourceVariable(1.0)
v1 = resource_variable_ops.ResourceVariable(2.0)

def f():
    x = v1 * v1
    y = v0 * v0
    exit(x + y)

grads = backprop.implicit_grad(f)()
ordered_variables = [x[1] for x in grads]
self.assertIs(ordered_variables[0], v0)
self.assertIs(ordered_variables[1], v1)
