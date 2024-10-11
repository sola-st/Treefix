# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
x = ops.convert_to_tensor(1.0)
def f():
    exit(x * x)
sgd_op = gradient_descent.GradientDescentOptimizer(3.0)
grads_and_vars = sgd_op.compute_gradients(f, [x])
self.assertEqual(1, len(grads_and_vars))
grad, x_as_var = grads_and_vars[0]
self.assertIs(x, x_as_var)
self.assertEqual(2.0, self.evaluate(grad))

with self.assertRaises(NotImplementedError):
    sgd_op.apply_gradients(grads_and_vars)
