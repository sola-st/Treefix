# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
"""Test if GPU CTC loss can fallback to the correct algorithm."""
if not test.is_gpu_available():
    self.skipTest("Need GPU for testing.")
if not context.executing_eagerly():
    self.skipTest("Need eager execution for testing.")
random_seed.set_random_seed(5)

batch_size = 1
num_labels = 11777
max_label_length = 2
num_frames = 1

labels = random_ops.random_uniform([batch_size, max_label_length],
                                   minval=1,
                                   maxval=num_labels,
                                   dtype=dtypes.int64)
logits = random_ops.random_uniform([num_frames, batch_size, num_labels])

label_length = random_ops.random_uniform([batch_size],
                                         minval=1,
                                         maxval=max_label_length,
                                         dtype=dtypes.int64)
logit_length = [num_frames] * batch_size

loss, grad = _ctc_loss_v3(labels, logits, label_length, logit_length, True)
ref_loss, ref_grad = _ctc_loss_v3(labels, logits, label_length,
                                  logit_length, False)

self.assertAllClose(loss, ref_loss, atol=1e-6)
self.assertAllClose(grad, ref_grad, atol=2e-6)
