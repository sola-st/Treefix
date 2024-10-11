# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/argmax_op_test.py
self._testArg(method, x, axis, expected_values, True, expected_err_re)
# Compilation time is too large with XLA/CPU autojit.
if not test_util.is_xla_enabled():
    self._testArg(method, x, axis, expected_values, False, expected_err_re)
