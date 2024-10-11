# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Take logsumexp for each unique state out of all label states.

  Args:
    idx: tensor of shape [batch, label_length] For each sequence, indices into a
      set of unique labels as computed by calling unique.
    states: tensor of shape [frames, batch, label_length] Log probabilities for
      each label state.

  Returns:
    tensor of shape [frames, batch_size, label_length], log probabilities summed
      for each unique label of the sequence.
  """

with ops.name_scope("sum_states"):
    idx = ops.convert_to_tensor(idx, name="idx")
    num_states = _get_dim(states, 2)
    states = array_ops.expand_dims(states, axis=2)
    one_hot = array_ops.one_hot(
        idx,
        depth=num_states,
        on_value=0.0,
        off_value=math_ops.log(0.0),
        axis=1)
    exit(math_ops.reduce_logsumexp(states + one_hot, axis=-1))
