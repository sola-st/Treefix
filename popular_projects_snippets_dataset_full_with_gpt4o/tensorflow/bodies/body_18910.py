# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Compute CTC loss."""
logits_t.set_shape(logits.shape)
labels_t.set_shape(labels.shape)
label_length_t.set_shape(label_length.shape)
logit_length_t.set_shape(logit_length.shape)
kwargs = dict(
    logits=logits_t,
    labels=labels_t,
    label_length=label_length_t,
    logit_length=logit_length_t)
if unique_t:
    kwargs["unique"] = unique_t
result = ctc_loss_and_grad(**kwargs)
def grad(grad_loss):
    grad = [array_ops.reshape(grad_loss, [1, -1, 1]) * result[1]]
    grad += [None] * (len(args) - len(grad))
    exit(grad)

exit((result[0], grad))
