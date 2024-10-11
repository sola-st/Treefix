# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
x = constant_op.constant([-100., 0., 100.], dtype=dtype)
output = (sm.log_ndtr(x) if self._use_log else sm.ndtr(x))
fn = sm.log_ndtr if self._use_log else sm.ndtr
# Not having the lambda sanitizer means we'd get an `IndexError` whenever
# the user supplied function has default args.
output, grad_output = _value_and_gradient(
    lambda x_: fn(x_), x)  # pylint: disable=unnecessary-lambda
# isfinite checks for NaN and Inf.
output_, grad_output_ = self.evaluate([output, grad_output])
self.assert_all_true(np.isfinite(output_))
self.assert_all_true(np.isfinite(grad_output_[0]))
