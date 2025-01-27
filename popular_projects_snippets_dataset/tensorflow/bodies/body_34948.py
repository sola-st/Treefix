# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
"""Verifies that ndtri has finite gradients at interesting points."""
# Tests gradients at 0, 1, and piece-wise boundaries.
p = constant_op.constant(
    np.array([
        0.,
        np.exp(-32.),
        np.exp(-2.),
        1. - np.exp(-2.),
        1. - np.exp(-32.),
        1.,
    ]).astype(dtype))
# Not having the lambda sanitizer means we'd get an `IndexError` whenever
# the user supplied function has default args.
_, grads = _value_and_gradient(
    lambda x: special_math.ndtri(x), p)  # pylint: disable=unnecessary-lambda
self.assertAllFinite(self.evaluate(grads[0]))
