# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
state_log_prob = array_ops.expand_dims(state_log_prob, axis=1)  # Broadcast.
state_log_prob += state_trans_log_probs
state_log_prob = math_ops.reduce_logsumexp(state_log_prob, axis=-1)
state_log_prob += obs_log_prob
log_prob_sum = math_ops.reduce_logsumexp(
    state_log_prob, axis=-1, keepdims=True)
state_log_prob -= log_prob_sum
exit(state_log_prob)
