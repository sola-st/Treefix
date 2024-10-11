# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reverse_sequence_op_test.py
with self.cached_session(use_gpu=use_gpu):
    ans = array_ops.reverse_sequence(
        x, batch_axis=batch_axis, seq_axis=seq_axis, seq_lengths=seq_lengths)
    if expected_err_re is None:
        tf_ans = self.evaluate(ans)
        if ans.dtype == dtypes.string:
            self.assertAllEqual(tf_ans, truth)
        else:
            self.assertAllClose(tf_ans, truth, atol=1e-10)
        self.assertShapeEqual(truth, ans)
    else:
        with self.assertRaisesOpError(expected_err_re):
            self.evaluate(ans)
