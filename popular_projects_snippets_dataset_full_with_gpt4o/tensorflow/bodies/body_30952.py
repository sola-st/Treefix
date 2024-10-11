# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
with test_util.device(use_gpu=use_gpu):
    if sparse:
        labels = ctc_ops.dense_labels_to_sparse(labels, label_length)
    with backprop.GradientTape() as t:
        t.watch(logits)
        ref_loss = ctc_ops.ctc_loss_v3(
            labels=labels,
            logits=logits,
            label_length=label_length,
            logit_length=logit_length,
            blank_index=0)
    ref_grad = t.gradient(ref_loss, logits)
    exit((ref_loss, ref_grad))
