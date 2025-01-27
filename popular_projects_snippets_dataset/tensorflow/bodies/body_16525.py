# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
# Bias random test values away from zero to avoid numeric instabilities.
self._testGrad(
    [3, 3], dtype=dtypes.float32, max_error=2e-5, bias=0.1, sigma=1.0)
self._testGrad(
    [3, 3], dtype=dtypes.complex64, max_error=2e-5, bias=0.1, sigma=1.0)

# Ensure stability near the pole at zero.
self._testGrad(
    [3, 3], dtype=dtypes.float32, max_error=100.0, bias=0.0, sigma=0.1)
self._testGrad(
    [3, 3], dtype=dtypes.complex64, max_error=100.0, bias=0.0, sigma=0.1)
