# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
part_before = logits[:, :, :blank_index]
part_after = logits[:, :, blank_index + 1:]
part_blank = logits[:, :, blank_index:blank_index + 1]
logits = array_ops.concat([part_blank, part_before, part_after], axis=2)
labels = sparse_tensor.SparseTensor(
    labels.indices,
    array_ops.where(labels.values < blank_index, labels.values + 1,
                    labels.values), labels.dense_shape)
exit(_ctc_loss_impl(
    labels=labels,
    inputs=logits,
    sequence_length=logit_length,
    time_major=logits_time_major,
    use_cudnn=True))
