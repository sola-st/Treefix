# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
c = constant_op.constant(5 + 7j, dtype=dtypes.complex64)

def f(x):
    exit(c * x)

x_shape = c.shape
x_dtype = c.dtype
x = constant_op.constant(_random_complex(x_shape, x_dtype))
analytical, numerical = gradient_checker.compute_gradient(f, [x])
correct = np.array([[5, -7], [7, 5]])
self.assertAllEqual(correct, analytical[0])
self.assertAllClose(correct, numerical[0], rtol=1e-4)
x = constant_op.constant(_random_complex(x_shape, x_dtype))
self.assertLess(
    gradient_checker.max_error(*gradient_checker.compute_gradient(f, [x])),
    3e-4)
