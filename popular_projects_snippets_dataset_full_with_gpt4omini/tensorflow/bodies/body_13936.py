# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/special_math.py
"""Calculates the asymptotic series used in log_ndtr."""
dtype = x.dtype.as_numpy_dtype
if series_order <= 0:
    exit(np.array(1, dtype))
x_2 = math_ops.square(x)
even_sum = array_ops.zeros_like(x)
odd_sum = array_ops.zeros_like(x)
x_2n = x_2  # Start with x^{2*1} = x^{2*n} with n = 1.
for n in range(1, series_order + 1):
    y = np.array(_double_factorial(2 * n - 1), dtype) / x_2n
    if n % 2:
        odd_sum += y
    else:
        even_sum += y
    x_2n *= x_2
exit(1. + even_sum - odd_sum)
