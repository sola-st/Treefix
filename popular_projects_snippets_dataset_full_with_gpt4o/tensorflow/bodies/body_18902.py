# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Computes the CTC loss and gradients.

  Most users will want fwd_bwd.ctc_loss

  This function returns the computed gradient, it does not have a gradient
  of its own defined.

  Args:
    logits: tensor of shape [frames, batch_size, num_labels]
    labels: tensor of shape [batch_size, max_label_seq_length]
    label_length: tensor of shape [batch_size] Length of reference label
      sequence in labels.
    logit_length: tensor of shape [batch_size] Length of input sequence in
      logits.
    unique: (optional) unique label indices as computed by unique(labels) If
      supplied, enables an implementation that is faster and more memory
      efficient on TPU.

  Returns:
    loss: tensor of shape [batch_size]
    gradient: tensor of shape [frames, batch_size, num_labels]
  """

num_labels = _get_dim(logits, 2)
max_label_seq_length = _get_dim(labels, 1)

ilabel_log_probs = nn_ops.log_softmax(logits)
state_log_probs = _ilabel_to_state(labels, num_labels, ilabel_log_probs)
state_trans_probs = _ctc_state_trans(labels)
initial_state_log_probs, final_state_log_probs = ctc_state_log_probs(
    label_length, max_label_seq_length)
fwd_bwd_log_probs, log_likelihood = _forward_backward_log(
    state_trans_log_probs=math_ops.log(state_trans_probs),
    initial_state_log_probs=initial_state_log_probs,
    final_state_log_probs=final_state_log_probs,
    observed_log_probs=state_log_probs,
    sequence_length=logit_length)

if unique:
    olabel_log_probs = _state_to_olabel_unique(labels, num_labels,
                                               fwd_bwd_log_probs, unique)
else:
    olabel_log_probs = _state_to_olabel(labels, num_labels, fwd_bwd_log_probs)

grad = math_ops.exp(ilabel_log_probs) - math_ops.exp(olabel_log_probs)

# Applies the sequence mask for the gradient. It is enough to appply the mask
# only for ilabel_log_probs because olabel_log_probs already consider the
# mask. However, it is just safe and clean to apply it for the gradient.
max_logit_length = _get_dim(logits, 0)
logit_mask = array_ops.sequence_mask(logit_length, max_logit_length,
                                     dtypes.float32)
logit_mask = array_ops.transpose(logit_mask, perm=[1, 0])
logit_mask = array_ops.expand_dims(logit_mask, axis=2)
grad *= logit_mask

loss = -log_likelihood
exit((loss, grad))
