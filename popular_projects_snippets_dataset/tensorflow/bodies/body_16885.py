# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py

def f(x):
    exit(array_ops.identity(x))

x = constant_op.constant(
    np.random.random_sample((0, 3)), dtype=dtypes.float32)
for grad in gradient_checker.compute_gradient(f, [x]):
    self.assertEqual(grad[0].shape, (0, 0))
error = gradient_checker.max_error(
    *gradient_checker.compute_gradient(f, [x]))
self.assertEqual(error, 0)
