# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
with ops.device("/GPU:0" if test.is_gpu_available() else "/CPU:0"):
    random_seed.set_random_seed(5)

    batch_size = 8
    num_labels = 6
    label_length = 5
    num_frames = 12
    logits = random_ops.random_uniform([num_frames, batch_size, num_labels])
    labels = random_ops.random_uniform(
        [batch_size, label_length], minval=0, maxval=num_labels-1,
        dtype=dtypes.int64)

    label_lengths = random_ops.random_uniform(
        [batch_size], minval=2, maxval=label_length, dtype=dtypes.int64)
    label_mask = array_ops.sequence_mask(
        label_lengths, maxlen=label_length, dtype=label_lengths.dtype)
    labels *= label_mask

    logit_lengths = [num_frames] * batch_size

    ctc_loss = ctc_ops.ctc_loss_dense(
        labels=labels,
        logits=logits,
        label_length=label_lengths,
        logit_length=logit_lengths,
        blank_index=-1)
    ctc_loss_grads = gradients_impl.gradients(ctc_loss, [logits])[0]

    tf_ctc_loss_labels = math_ops.cast(labels, dtypes.int32)
    tf_ctc_loss_labels = ctc_ops.dense_labels_to_sparse(
        tf_ctc_loss_labels, label_lengths)

    tf_nn_ctc_loss = ctc_ops.ctc_loss(
        labels=tf_ctc_loss_labels,
        inputs=logits,
        sequence_length=logit_lengths,
        time_major=True)
    tf_nn_ctc_grads = gradients_impl.gradients(tf_nn_ctc_loss, [logits])[0]

    with self.cached_session() as sess:
        for _ in range(32):
            self.assertAllClose(*self.evaluate([ctc_loss, tf_nn_ctc_loss]))
            self.assertAllClose(
                *self.evaluate([ctc_loss_grads, tf_nn_ctc_grads]),
                rtol=2e-06,
                atol=2e-06)
