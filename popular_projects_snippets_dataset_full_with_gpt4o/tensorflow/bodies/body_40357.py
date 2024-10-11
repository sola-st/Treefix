# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def fn(x):
    b = constant_op.constant(2.0)
    c = math_ops.add(x, b)
    exit(math_ops.add(c, constant_op.constant(3.0)))

grad = backprop.gradients_function(fn, [0])(constant_op.constant(1.0))[0]
self.assertAllEqual(grad, 1.0)
