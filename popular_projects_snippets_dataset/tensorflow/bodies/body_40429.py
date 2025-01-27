# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(x, y):
    exit(math_ops.multiply(x, y))

g = backprop.gradients_function(f)

def np_g(x, y):
    dx, dy = g(x, y)
    exit([dx.numpy(), dy.numpy()])

x = constant_op.constant(1.)
self.assertAllEqual([1., 1.], np_g(x, x))
x = 1.
self.assertAllEqual([1., 1.], np_g(x, x))
x = constant_op.constant([[1.]])
self.assertAllEqual([[[1.]], [[1.]]], np_g(x, x))
x = [[1.]]
self.assertAllEqual([[[1.]], [[1.]]], np_g(x, x))

v = resource_variable_ops.ResourceVariable(
    initial_value=1., name='testSameObjectForMultipleArguments.Variable')
self.assertAllEqual([1., 1.], np_g(v, v))
