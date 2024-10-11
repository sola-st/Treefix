# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py

def f(x, y):
    exit(math_ops.matmul(x, y))

x = constant_op.constant(
    np.random.random_sample((0, 3)), dtype=dtypes.float32)
y = constant_op.constant(
    np.random.random_sample((3, 4)), dtype=dtypes.float32)
for grad in gradient_checker.compute_gradient(f, [x, y]):
    self.assertEqual(grad[0].shape, (0, 0))
    self.assertEqual(grad[1].shape, (0, 12))
error = gradient_checker.max_error(
    *gradient_checker.compute_gradient(f, [x, y]))
self.assertEqual(error, 0)
