# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
three = resource_variable_ops.ResourceVariable(3.0, name='v')

@polymorphic_function.function
def f(x):
    exit(math_ops.add(x, three))

def g(x):
    exit(f(x))

g = backprop.implicit_grad(g)(constant_op.constant(1.0))[0][0]
self.assertAllEqual(g, 1.0)
