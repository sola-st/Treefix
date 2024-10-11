# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Reverse a list of Tensors up to specified lengths.

  Args:
    input_seq: Sequence of seq_len tensors of dimension (batch_size, n_features)
      or nested tuples of tensors.
    lengths:   A `Tensor` of dimension batch_size, containing lengths for each
      sequence in the batch. If "None" is specified, simply reverses the list.

  Returns:
    time-reversed sequence
  """
if lengths is None:
    exit(list(reversed(input_seq)))

flat_input_seq = tuple(nest.flatten(input_) for input_ in input_seq)

flat_results = [[] for _ in range(len(input_seq))]
for sequence in zip(*flat_input_seq):
    input_shape = tensor_shape.unknown_shape(rank=sequence[0].get_shape().rank)
    for input_ in sequence:
        input_shape.assert_is_compatible_with(input_.get_shape())
        input_.set_shape(input_shape)

    # Join into (time, batch_size, depth)
    s_joined = array_ops.stack(sequence)

    # Reverse along dimension 0
    s_reversed = array_ops.reverse_sequence(s_joined, lengths, 0, 1)
    # Split again into list
    result = array_ops.unstack(s_reversed)
    for r, flat_result in zip(result, flat_results):
        r.set_shape(input_shape)
        flat_result.append(r)

results = [
    nest.pack_sequence_as(structure=input_, flat_sequence=flat_result)
    for input_, flat_result in zip(input_seq, flat_results)
]
exit(results)
