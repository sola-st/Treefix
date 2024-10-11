# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
batch_size = 8
num_labels = 6
max_label_length = 5
num_frames = 12

labels = np.random.randint(1, num_labels, [batch_size, max_label_length])
labels = ops.convert_to_tensor(labels, dtypes.int64)
fp16_logits = np.random.uniform(size=[num_frames, batch_size, num_labels])
fp16_logits = ops.convert_to_tensor(fp16_logits, dtypes.float16)
label_length = np.random.randint(2, max_label_length, [batch_size])
label_length = ops.convert_to_tensor(label_length, dtypes.int64)

label_mask = array_ops.sequence_mask(
    label_length, maxlen=max_label_length, dtype=label_length.dtype)
labels *= label_mask
logit_length = [num_frames] * batch_size

fp16_loss, fp16_grad = _ctc_loss_v3(
    labels, fp16_logits, label_length, logit_length, use_gpu=True,
    sparse=sparse_labels)
fp32_loss, fp32_grad = _ctc_loss_v3(
    labels, math_ops.cast(fp16_logits, dtypes.float32), label_length,
    logit_length, use_gpu=True, sparse=sparse_labels)

self.assertEqual(fp16_loss.dtype, dtypes.float16)
self.assertEqual(fp16_grad.dtype, dtypes.float16)
self.assertAllClose(
    self.evaluate(fp16_loss),
    self.evaluate(math_ops.cast(fp32_loss, dtypes.float16))
)
self.assertAllClose(
    self.evaluate(fp16_grad),
    self.evaluate(math_ops.cast(fp32_grad, dtypes.float16))
)
