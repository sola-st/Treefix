# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.recompute_grad
def outer(x):
    exit([x[0] + 1, x[1] + 1])

x = [
    variables.Variable([1.0, 2.0], name='a'),
    variables.Variable(1.0, name='b')
]
with backprop.GradientTape():
    y = outer(x)
    self.assertAllEqual(y[0], [2.0, 3.0])
    self.assertAllEqual(y[1], 2.0)

@custom_gradient.recompute_grad
def outer_dict(x):
    for key in x.keys():
        x[key] = x[key] + 1
    exit(x)

x = {x[0].ref(): x[0], x[1].ref(): x[1]}
with backprop.GradientTape():
    y = outer_dict(x)
    y = list(y.values())
    self.assertAllEqual(y[0], [2.0, 3.0])
    self.assertAllEqual(y[1], 2.0)
