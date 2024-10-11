# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
"""Validate FractionalAvgPool's result against expected.

    Expected result is computed given input_tensor, and pooling region defined
    by row_seq and col_seq.

    Args:
      input_tensor: A tensor or numpy ndarray.
      pooling_ratio: A list or tuple of length 4, first and last element be 1.
      pseudo_random: Use pseudo random method to generate pooling sequence.
      overlapping: Use overlapping when pooling.

    Returns:
      None
    """
with self.cached_session() as sess:
    p, r, c = nn_ops.fractional_avg_pool_v2(
        input_tensor,
        pooling_ratio,
        pseudo_random,
        overlapping,
        seed=self._SEED)
    actual, row_seq, col_seq = self.evaluate([p, r, c])
    expected = self._GetExpectedFractionalAvgPoolResult(input_tensor, row_seq,
                                                        col_seq, overlapping)
    self.assertShapeEqual(expected, p)
    self.assertAllClose(expected, actual)
