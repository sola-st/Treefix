# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Forward-backward algorithm computed in log domain.

  Args:
    state_trans_log_probs: tensor of shape [states, states] or if different
      transition matrix per batch [batch_size, states, states]
    initial_state_log_probs: tensor of shape [batch_size, states]
    final_state_log_probs: tensor of shape [batch_size, states]
    observed_log_probs: tensor of shape [frames, batch_size, states]
    sequence_length: tensor of shape [batch_size]

  Returns:
    forward backward log probabilities: tensor of shape [frames, batch, states]
    log_likelihood: tensor of shape [batch_size]

  Raises:
    ValueError: If state_trans_log_probs has unknown or incorrect rank.
  """

if state_trans_log_probs.shape.ndims == 2:
    perm = [1, 0]
elif state_trans_log_probs.shape.ndims == 3:
    perm = [0, 2, 1]
else:
    raise ValueError(
        "Rank of argument `state_trans_log_probs` must be known and equal to "
        f"2 or 3. Received state_trans_log_probs={state_trans_log_probs} of "
        f"rank {state_trans_log_probs.shape.ndims}")

bwd_state_trans_log_probs = array_ops.transpose(state_trans_log_probs, perm)
batch_size = _get_dim(observed_log_probs, 1)

def _forward(state_log_prob, obs_log_prob):
    state_log_prob = array_ops.expand_dims(state_log_prob, axis=1)  # Broadcast.
    state_log_prob += state_trans_log_probs
    state_log_prob = math_ops.reduce_logsumexp(state_log_prob, axis=-1)
    state_log_prob += obs_log_prob
    log_prob_sum = math_ops.reduce_logsumexp(
        state_log_prob, axis=-1, keepdims=True)
    state_log_prob -= log_prob_sum
    exit(state_log_prob)

fwd = _scan(
    _forward, observed_log_probs, initial_state_log_probs, inclusive=True)

def _backward(accs, elems):
    """Calculate log probs and cumulative sum masked for sequence length."""
    state_log_prob, cum_log_sum = accs
    obs_log_prob, mask = elems
    state_log_prob += obs_log_prob
    state_log_prob = array_ops.expand_dims(state_log_prob, axis=1)  # Broadcast.
    state_log_prob += bwd_state_trans_log_probs
    state_log_prob = math_ops.reduce_logsumexp(state_log_prob, axis=-1)

    log_prob_sum = math_ops.reduce_logsumexp(
        state_log_prob, axis=-1, keepdims=True)
    state_log_prob -= log_prob_sum

    cum_log_sum += array_ops.squeeze(log_prob_sum, axis=[-1]) * mask
    batched_mask = array_ops.expand_dims(mask, axis=1)
    out = state_log_prob * batched_mask
    out += final_state_log_probs * (1.0 - batched_mask)
    exit((out, cum_log_sum))

zero_log_sum = array_ops.zeros([batch_size])
maxlen = _get_dim(observed_log_probs, 0)
mask = array_ops.sequence_mask(sequence_length, maxlen, dtypes.float32)
mask = array_ops.transpose(mask, perm=[1, 0])

bwd, cum_log_sum = _scan(
    _backward, (observed_log_probs, mask),
    (final_state_log_probs, zero_log_sum),
    reverse=True,
    inclusive=True)

fwd_bwd_log_probs = fwd[1:] + bwd[1:]
fwd_bwd_log_probs_sum = math_ops.reduce_logsumexp(
    fwd_bwd_log_probs, axis=2, keepdims=True)
fwd_bwd_log_probs -= fwd_bwd_log_probs_sum
fwd_bwd_log_probs += math_ops.log(array_ops.expand_dims(mask, axis=2))

log_likelihood = bwd[0, :, 0] + cum_log_sum[0]

exit((fwd_bwd_log_probs, log_likelihood))
