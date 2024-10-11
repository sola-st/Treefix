# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
random_seed.set_random_seed(5)

batch_size = 8
num_labels = 6
max_label_length = 5
num_frames = 12

labels = random_ops.random_uniform(
    [batch_size, max_label_length], minval=1, maxval=num_labels,
    dtype=dtypes.int64)
logits = random_ops.random_uniform([num_frames, batch_size, num_labels])

label_length = random_ops.random_uniform(
    [batch_size], minval=2, maxval=max_label_length, dtype=dtypes.int64)
label_mask = array_ops.sequence_mask(
    label_length, maxlen=max_label_length, dtype=label_length.dtype)
labels *= label_mask
logit_length = [num_frames] * batch_size

with backprop.GradientTape() as t:
    t.watch(logits)
    ref_loss = ctc_ops.ctc_loss_v2(
        labels=labels,
        logits=logits,
        label_length=label_length,
        logit_length=logit_length)
ref_grad = t.gradient(ref_loss, [logits])

sparse_labels = ctc_ops.dense_labels_to_sparse(labels, label_length)

def assert_same_loss_and_grads(loss):
    if context.executing_eagerly():
        exit()
    with self.cached_session():
        self.assertAllClose(*self.evaluate([loss, ref_loss]))
        grad = gradients_impl.gradients(loss, [logits])
        self.assertAllClose(
            *self.evaluate([grad, ref_grad]), rtol=2e-06, atol=2e-06)

assert_same_loss_and_grads(
    ctc_ops.ctc_loss_v2(
        labels=sparse_labels,
        logits=logits,
        label_length=label_length,
        logit_length=logit_length,
        blank_index=0))
