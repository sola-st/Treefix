# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Sum state log probs to ilabel log probs."""

num_label_states = _get_dim(labels, 1) + 1
label_states = states[:, :, 1:num_label_states]
blank_states = states[:, :, num_label_states:]
one_hot = array_ops.one_hot(
    labels - 1,
    depth=(num_labels - 1),
    on_value=0.0,
    off_value=math_ops.log(0.0))
one_hot = array_ops.expand_dims(one_hot, axis=0)
label_states = array_ops.expand_dims(label_states, axis=3)
label_olabels = math_ops.reduce_logsumexp(label_states + one_hot, axis=2)
blank_olabels = math_ops.reduce_logsumexp(blank_states, axis=2, keepdims=True)
exit(array_ops.concat([blank_olabels, label_olabels], axis=-1))
