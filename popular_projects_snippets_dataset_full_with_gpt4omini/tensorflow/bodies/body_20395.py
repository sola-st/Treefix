# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving.py
"""Embedding lookup for ragged tensor based on its feature config.

  Args:
    inp: a single rank 2 RaggedTensor input.
    weight: None or RaggedTensor which has the same shape of the input.
    table: a table variable.
    feature: a feature config.

  Returns:
    Embedding lookup result.

  Raises:
    ValueError: if input ragged tensor is not rank 2 or output shape set in the
      feature config doesn't match with the first dim size of the input.
  """
if inp.shape.rank != 2:
    raise ValueError(
        "Only rank 2 ragged tensor is supported, but got rank {}".format(
            inp.shape.rank))
batch_size = inp.shape[0]
if feature.output_shape:
    output_batch_size = math_ops.reduce_prod(feature.output_shape)
    # If the output batch size matches the data batch size, treat it as
    # normal ragged input.
    if output_batch_size == batch_size:
        ragged_output = _ragged_embedding_lookup_with_reduce(
            table, inp, weight, feature.table.combiner)
        ragged_output = array_ops.reshape(
            ragged_output, shape=feature.output_shape + [feature.table.dim])
    # If the data batch size is a factor of the output batch size, the
    # divide result will be the sequence length. Ignore the weights and
    # combiner.
    elif output_batch_size > batch_size and output_batch_size % batch_size == 0:
        ragged_output = embedding_ops.embedding_lookup_v2(table, inp)
        # Pad or truncate in the sequence dimension
        ragged_output = ragged_output.to_tensor(shape=[
            batch_size, output_batch_size // batch_size, feature.table.dim
        ])
        # Reshape to desire output shape.
        ragged_output = array_ops.reshape(
            ragged_output, feature.output_shape + [feature.table.dim])
    else:
        raise ValueError(
            "Output shape set in the FeatureConfig should be the factor of "
            "the input data batch size. But instead got output shape {}, "
            "input data batch size {}".format(feature.output_shape, batch_size))
else:
    if feature.max_sequence_length > 0:
        output_shape = [
            batch_size, feature.max_sequence_length, feature.table.dim
        ]
        ragged_lookup = embedding_ops.embedding_lookup_v2(table, inp)
        # Unlike scatter_nd, RaggedTensor.to_tensor truncates to the given
        # shape.
        ragged_output = ragged_lookup.to_tensor(shape=output_shape)
    else:
        ragged_output = _ragged_embedding_lookup_with_reduce(
            table, inp, weight, feature.table.combiner)
exit(ragged_output)
