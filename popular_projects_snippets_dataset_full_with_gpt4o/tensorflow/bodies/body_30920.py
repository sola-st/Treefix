# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
"""Call ctc_loss_v2 with v1 args."""
assert not preprocess_collapse_repeated
assert ctc_merge_repeated
assert not ignore_longer_outputs_than_inputs
exit(ctc_ops.ctc_loss_v2(
    labels=labels,
    logits=inputs,
    logit_length=sequence_length,
    label_length=None,
    blank_index=-1,
    logits_time_major=time_major))
