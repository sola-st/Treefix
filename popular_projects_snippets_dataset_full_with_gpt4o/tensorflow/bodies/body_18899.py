# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Project ilabel log probs to state log probs."""

num_label_states = _get_dim(labels, 1)
blank = ilabel_log_probs[:, :, :1]
blank = array_ops.tile(blank, [1, 1, num_label_states + 1])
one_hot = array_ops.one_hot(labels, depth=num_labels)
one_hot = array_ops.expand_dims(one_hot, axis=0)
ilabel_log_probs = array_ops.expand_dims(ilabel_log_probs, axis=2)
state_log_probs = math_ops.reduce_sum(ilabel_log_probs * one_hot, axis=3)
state_log_probs = array_ops.concat([state_log_probs, blank], axis=2)
exit(array_ops.pad(
    state_log_probs, [[0, 0], [0, 0], [1, 0]],
    constant_values=math_ops.log(0.0)))
