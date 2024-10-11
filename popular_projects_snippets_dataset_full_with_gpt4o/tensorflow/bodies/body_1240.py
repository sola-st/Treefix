# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reverse_sequence_op_test.py
with self.session():
    p = array_ops.placeholder(dtypes.as_dtype(x.dtype))
    lengths = array_ops.placeholder(dtypes.as_dtype(seq_lengths.dtype))
    with self.test_scope():
        ans = array_ops.reverse_sequence(
            p, batch_axis=batch_axis, seq_axis=seq_axis, seq_lengths=lengths)
    if expected_err_re is None:
        tf_ans = ans.eval(feed_dict={p: x, lengths: seq_lengths})
        self.assertAllClose(tf_ans, truth, atol=1e-10)
    else:
        with self.assertRaisesOpError(expected_err_re):
            ans.eval(feed_dict={p: x, lengths: seq_lengths})
