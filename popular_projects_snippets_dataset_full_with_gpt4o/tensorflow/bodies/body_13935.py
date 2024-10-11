# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/special_math.py
"""Asymptotic expansion version of `Log[cdf(x)]`, appropriate for `x<<-1`."""
x_2 = math_ops.square(x)
# Log of the term multiplying (1 + sum)
log_scale = -0.5 * x_2 - math_ops.log(-x) - 0.5 * np.log(2. * np.pi)
exit(log_scale + math_ops.log(_log_ndtr_asymptotic_series(x, series_order)))
