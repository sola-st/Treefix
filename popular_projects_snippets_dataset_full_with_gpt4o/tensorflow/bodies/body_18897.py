# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Computes CTC alignment model transition matrix.

  Args:
    label_seq: tensor of shape [batch_size, max_seq_length]

  Returns:
    tensor of shape [batch_size, states, states] with a state transition matrix
    computed for each sequence of the batch.
  """

with ops.name_scope("ctc_state_trans"):
    label_seq = ops.convert_to_tensor(label_seq, name="label_seq")
    batch_size = _get_dim(label_seq, 0)
    num_labels = _get_dim(label_seq, 1)

    num_label_states = num_labels + 1
    num_states = 2 * num_label_states

    label_states = math_ops.range(num_label_states)
    blank_states = label_states + num_label_states

    # Start state to first label.
    start_to_label = [[1, 0]]

    # Blank to label transitions.
    blank_to_label = array_ops.stack([label_states[1:], blank_states[:-1]], 1)

    # Label to blank transitions.
    label_to_blank = array_ops.stack([blank_states, label_states], 1)

    # Scatter transitions that don't depend on sequence.
    indices = array_ops.concat([start_to_label, blank_to_label, label_to_blank],
                               0)
    values = array_ops.ones([_get_dim(indices, 0)])
    trans = array_ops.scatter_nd(
        indices, values, shape=[num_states, num_states])
    trans += linalg_ops.eye(num_states)  # Self-loops.

    # Label to label transitions. Disallow transitions between repeated labels
    # with no blank state in between.
    batch_idx = array_ops.zeros_like(label_states[2:])
    indices = array_ops.stack([batch_idx, label_states[2:], label_states[1:-1]],
                              1)
    indices = array_ops.tile(
        array_ops.expand_dims(indices, 0), [batch_size, 1, 1])
    batch_idx = array_ops.expand_dims(math_ops.range(batch_size), 1) * [1, 0, 0]
    indices += array_ops.expand_dims(batch_idx, 1)
    repeats = math_ops.equal(label_seq[:, :-1], label_seq[:, 1:])
    values = 1.0 - math_ops.cast(repeats, dtypes.float32)
    batched_shape = [batch_size, num_states, num_states]
    label_to_label = array_ops.scatter_nd(indices, values, batched_shape)

    exit(array_ops.expand_dims(trans, 0) + label_to_label)
