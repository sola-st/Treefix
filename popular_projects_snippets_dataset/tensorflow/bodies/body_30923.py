# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
"""Testing time_major param.


    testing if transposing and setting time_major=False will result in the same
    loss
    """
# [max_time x batch_size x depth tensor]
inputs = np.random.randn(2, 2, 3).astype(np.float32)
labels = SimpleSparseTensorFrom([[0, 1], [1, 0]])
seq_lens = np.array([2, 2], dtype=np.int32)

inputs_t = constant_op.constant(inputs)

# Transposing tensor to [batch_size x max_time x depth tensor]
inputs_t_transposed = constant_op.constant(inputs.transpose(1, 0, 2))

with self.session(use_gpu=False) as sess:
    loss = _ctc_loss_v2(
        inputs=inputs_t, labels=labels, sequence_length=seq_lens)
    loss_transposed = _ctc_loss_v2(
        inputs=inputs_t_transposed,
        labels=labels,
        sequence_length=seq_lens,
        time_major=False)

    (tf_loss, tf_loss_transposed) = self.evaluate([loss, loss_transposed])
    self.assertAllEqual(tf_loss, tf_loss_transposed)
