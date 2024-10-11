# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops_test.py
original_rt = ragged_factory_ops.constant(original)
expected_rt = ragged_factory_ops.constant(expected)
actual = ragged_math_ops.ragged_cumsum(
    original_rt, axis=axis, exclusive=exclusive, reverse=reverse)
self.assertAllEqual(actual, expected_rt)
baseline = _cumsum_slow(original_rt, axis=axis, exclusive=exclusive,
                        reverse=reverse)
self.assertAllEqual(baseline, expected_rt)
