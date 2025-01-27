# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
unique_labels = ctc_ops.ctc_unique_labels(labels) if unique else None
exit(ctc_ops.ctc_loss_dense(
    labels=labels,
    logits=logits,
    label_length=label_lengths,
    logit_length=logit_lengths,
    unique=unique_labels,
    blank_index=blank_index))
