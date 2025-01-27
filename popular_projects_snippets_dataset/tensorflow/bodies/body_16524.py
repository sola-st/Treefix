# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
np.random.seed(7)
if dtype in (dtypes.complex64, dtypes.complex128):
    value = math_ops.complex(
        self._biasedRandN(
            shape, bias=bias, sigma=sigma),
        self._biasedRandN(
            shape, bias=bias, sigma=sigma))
else:
    value = ops.convert_to_tensor(
        self._biasedRandN(
            shape, bias=bias), dtype=dtype)

with self.cached_session():
    output = math_ops.abs(value)
    error = gradient_checker.compute_gradient_error(
        value, shape, output, output.get_shape().as_list())
self.assertLess(error, max_error)
