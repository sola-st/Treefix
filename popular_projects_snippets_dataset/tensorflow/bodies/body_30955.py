# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
batch_size = 8
num_labels = 6
max_label_length = 5
num_frames = 12

labels = np.random.randint(1, num_labels, [batch_size, max_label_length])
labels = ops.convert_to_tensor(labels, dtypes.int64)
logits = np.random.uniform(size=[num_frames, batch_size, num_labels])
label_length = np.random.randint(2, max_label_length, [batch_size])
label_length = ops.convert_to_tensor(label_length, dtypes.int64)

label_mask = array_ops.sequence_mask(
    label_length, maxlen=max_label_length, dtype=label_length.dtype)
labels *= label_mask
logit_length = [num_frames] * batch_size
if sparse_labels:
    labels = ctc_ops.dense_labels_to_sparse(labels, label_length)

list_loss = ctc_ops.ctc_loss_v3(
    labels=labels,
    logits=logits.tolist(),
    label_length=label_length,
    logit_length=logit_length,
    blank_index=0)
tensor_loss = ctc_ops.ctc_loss_v3(
    labels=labels,
    logits=ops.convert_to_tensor(logits, dtypes.float32),
    label_length=label_length,
    logit_length=logit_length,
    blank_index=0)

self.assertAllClose(self.evaluate(list_loss), self.evaluate(tensor_loss))
