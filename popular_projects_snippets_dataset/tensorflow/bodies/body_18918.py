# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
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
