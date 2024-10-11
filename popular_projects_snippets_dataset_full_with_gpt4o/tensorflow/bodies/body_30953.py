# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
"""Testing GPU CTC loss.


    testing if GPU CTC loss will generate same result with CPU version
    """
if not test.is_gpu_available():
    self.skipTest("Need GPU for testing.")
if not context.executing_eagerly():
    self.skipTest("Need eager execution for testing.")
random_seed.set_random_seed(5)

batch_size = 8
num_labels = 6
max_label_length = 5
num_frames = 12

labels = random_ops.random_uniform([batch_size, max_label_length],
                                   minval=1,
                                   maxval=num_labels,
                                   dtype=dtypes.int64)
logits = random_ops.random_uniform([num_frames, batch_size, num_labels])

label_length = random_ops.random_uniform([batch_size],
                                         minval=2,
                                         maxval=max_label_length,
                                         dtype=dtypes.int64)
label_mask = array_ops.sequence_mask(
    label_length, maxlen=max_label_length, dtype=label_length.dtype)
labels *= label_mask
logit_length = [num_frames] * batch_size

if run_tf_func:
    ctc_loss = def_function.function(_ctc_loss_v3)
else:
    ctc_loss = _ctc_loss_v3

ref_loss, ref_grad = ctc_loss(labels, logits, label_length, logit_length,
                              False)
loss, grad = ctc_loss(labels, logits, label_length, logit_length, True)

self.assertAllClose(loss, ref_loss, atol=1e-6)
self.assertAllClose(grad, ref_grad, atol=2e-6)
