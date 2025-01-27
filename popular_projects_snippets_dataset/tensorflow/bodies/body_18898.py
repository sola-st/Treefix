# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Computes CTC alignment initial and final state log probabilities.

  Create the initial/final state values directly as log values to avoid
  having to take a float64 log on tpu (which does not exist).

  Args:
    seq_lengths: int tensor of shape [batch_size], seq lengths in the batch.
    max_seq_length: int, max sequence length possible.

  Returns:
    initial_state_log_probs, final_state_log_probs
  """

batch_size = _get_dim(seq_lengths, 0)
num_label_states = max_seq_length + 1
num_duration_states = 2
num_states = num_duration_states * num_label_states
log_0 = math_ops.cast(
    math_ops.log(math_ops.cast(0, dtypes.float64) + 1e-307), dtypes.float32)

initial_state_log_probs = array_ops.one_hot(
    indices=array_ops.zeros([batch_size], dtype=dtypes.int32),
    depth=num_states,
    on_value=0.0,
    off_value=log_0,
    axis=1)

label_final_state_mask = array_ops.one_hot(
    seq_lengths, depth=num_label_states, axis=0)
duration_final_state_mask = array_ops.ones(
    [num_duration_states, 1, batch_size])
final_state_mask = duration_final_state_mask * label_final_state_mask
final_state_log_probs = (1.0 - final_state_mask) * log_0
final_state_log_probs = array_ops.reshape(final_state_log_probs,
                                          [num_states, batch_size])

exit((initial_state_log_probs, array_ops.transpose(final_state_log_probs)))
