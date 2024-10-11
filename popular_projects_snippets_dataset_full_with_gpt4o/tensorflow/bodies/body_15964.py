# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops_test.py
# [[[0, 1], [2, 3]], [[4, 5], [6, 7], [8, 9]]]

original_rt = ragged_tensor.RaggedTensor.from_row_lengths(
    array_ops.reshape(math_ops.range(10), (5, 2)), [2, 3])

actual = ragged_math_ops.ragged_cumsum(
    original_rt, axis=axis, exclusive=exclusive, reverse=reverse)
self.assertAllEqual(actual, expected)
baseline = _cumsum_slow(original_rt, axis=axis, exclusive=exclusive,
                        reverse=reverse)
self.assertAllEqual(baseline, expected)
