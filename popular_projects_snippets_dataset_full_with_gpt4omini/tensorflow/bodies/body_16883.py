# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py

def f(x):
    exit(math_ops.conj(x))

x_shape = ()
x_dtype = dtypes.complex64
x = constant_op.constant(_random_complex(x_shape, x_dtype))
analytical, numerical = gradient_checker.compute_gradient(f, [x])
correct = np.array([[1, 0], [0, -1]])
self.assertAllEqual(correct, analytical[0])
self.assertAllClose(correct, numerical[0], rtol=2e-5)
x = constant_op.constant(_random_complex(x_shape, x_dtype))
self.assertLess(
    gradient_checker.max_error(*gradient_checker.compute_gradient(f, [x])),
    2e-5)
