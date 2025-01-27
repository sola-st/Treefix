# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
random_seed.set_random_seed(5)

batch_size = 8
num_labels = 6
label_length = 5
num_frames = 12
logits = random_ops.random_uniform([num_frames, batch_size, num_labels])
labels = random_ops.random_uniform(
    [batch_size, label_length], minval=1, maxval=num_labels,
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
    unique=ctc_ops.ctc_unique_labels(labels))
ctc_loss_grads = gradients_impl.gradients(ctc_loss, [logits])[0]

# Shift labels down by one (move blank from 0 to num_labels -1)
tf_ctc_loss_labels = math_ops.cast(labels, dtypes.int32) - 1
tf_nn_ctc_logits = array_ops.concat([
    logits[:, :, 1:],
    logits[:, :, 0:1],
], axis=2)

tf_ctc_loss_labels = ctc_ops.dense_labels_to_sparse(
    tf_ctc_loss_labels, label_lengths)

tf_nn_ctc_loss = ctc_ops.ctc_loss(
    labels=tf_ctc_loss_labels,
    inputs=tf_nn_ctc_logits,
    sequence_length=logit_lengths,
    time_major=True)
tf_nn_ctc_grads = gradients_impl.gradients(tf_nn_ctc_loss, [logits])[0]

with self.cached_session():
    for _ in range(32):
        self.assertAllClose(*self.evaluate([ctc_loss, tf_nn_ctc_loss]))
        self.assertAllClose(
            *self.evaluate([ctc_loss_grads, tf_nn_ctc_grads]),
            rtol=2e-06,
            atol=2e-06)
