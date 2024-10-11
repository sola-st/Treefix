# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
"""Runs the operation in one session with different input tensor shapes."""
with self.cached_session() as sess:
    input_holder = array_ops.placeholder(dtypes.float32,
                                         [None, None, None, 3])
    pooling_ratio = [1, 1.5, 1.5, 1]
    pseudo_random = False
    overlapping = False
    p, r, c = nn_ops.fractional_avg_pool_v2(
        input_holder,
        pooling_ratio,
        pseudo_random,
        overlapping,
        seed=self._SEED)
    # First run.
    input_a = np.zeros([3, 32, 32, 3])
    actual, row_seq, col_seq = sess.run([p, r, c], {input_holder: input_a})
    expected = self._GetExpectedFractionalAvgPoolResult(
        input_a, row_seq, col_seq, overlapping)
    self.assertSequenceEqual(expected.shape, actual.shape)
    # Second run.
    input_b = np.zeros([4, 60, 60, 3])
    actual, row_seq, col_seq = sess.run([p, r, c], {input_holder: input_b})
    expected = self._GetExpectedFractionalAvgPoolResult(
        input_b, row_seq, col_seq, overlapping)
    self.assertSequenceEqual(expected.shape, actual.shape)
