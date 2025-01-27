# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
assert num_frames >= max_label_sequence_length

labels_shape = (batch_size, max_label_sequence_length)
# Zero-pad the labels. Zero is the default blank index in the TF2 API.
# num_classes includes the blank class
unmasked_labels = np.random.randint(
    1, num_classes, size=labels_shape, dtype=np.int32)
labels_lengths = np.random.randint(
    1, high=max_label_sequence_length, size=batch_size, dtype=np.int32)
labels_masks = (np.arange(max_label_sequence_length) <
                labels_lengths.reshape(batch_size, 1)).astype(np.int32)
labels = unmasked_labels * labels_masks
if sparse_labels:
    labels = ctc_ops.dense_labels_to_sparse(labels, labels_lengths)

if logits_time_major:
    logits_shape = (num_frames, batch_size, num_classes)
else:
    logits_shape = (batch_size, num_frames, num_classes)
logits = self._randomFloats(logits_shape)

labels_lengths = constant_op.constant(labels_lengths)

logits_lengths = [num_frames] * batch_size
logits_lengths = constant_op.constant(logits_lengths)

exit((labels, logits, labels_lengths, logits_lengths))
