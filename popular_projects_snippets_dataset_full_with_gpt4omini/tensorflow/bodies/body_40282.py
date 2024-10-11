# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = resource_variable_ops.ResourceVariable(
    initial_value=constant_op.constant(1.0), name='x')

def fn():
    b = constant_op.constant(2.0)
    c = math_ops.add(x.value(), b)
    exit(math_ops.add(c, constant_op.constant(3.0)))

grads_and_vars = backprop.implicit_grad(fn)()
self.assertAllEqual(grads_and_vars[0][0], 1.0)
self.assertAllEqual(id(grads_and_vars[0][1]), id(x))
