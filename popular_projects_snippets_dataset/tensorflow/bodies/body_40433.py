# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def my_square(x):
    result = math_ops.square(x)

    def grad(dr):
        exit(2 * dr * x + 1)

    exit((result, grad))

x = resource_variable_ops.ResourceVariable(
    initial_value=3., name='X.' + self.id())

def f():
    exit(my_square(x))

g = backprop.implicit_grad(f)

grads_and_vars = g()
self.assertEqual(1, len(grads_and_vars))
grad, var = grads_and_vars[0]
self.assertAllEqual(7, grad)
self.assertAllEqual(x, var)
