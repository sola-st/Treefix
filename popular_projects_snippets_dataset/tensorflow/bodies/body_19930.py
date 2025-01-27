# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
"""Embedding lookup for ragged tensor based on its feature config.

    Args:
      inp: a single rank 2 RaggedTensor input.
      weight: None or RaggedTensor which has the same shape of the input.
      table: a table variable.
      feature: a feature config.

    Returns:
      Embedding lookup result.

    Raises:
      ValueError: if input ragged tensor is not rank 2 or output shape set in
      the feature config doesn't match with the first dim size of the input.
    """
if inp.shape.rank != 2:
    raise ValueError(
        "Only rank 2 ragged tensor is supported, but got rank {}".format(
            inp.shape.rank))
batch_size = inp.shape[0]

# This computation needs to placed outside of tpu as the size of the row
# splits and values can change for different batch which can cause
# the program to re-compile.
def ragged_to_dense_outside_compilation(inp, weight, batch_size, feature):
    if weight is None:
        weight = ragged_tensor.RaggedTensor.from_row_splits(
            array_ops.ones_like(inp.values, dtype=dtypes.float32),
            inp.row_splits)
    if not feature.output_shape and feature.max_sequence_length > 0:
        inp = inp.to_tensor(shape=(batch_size, feature.max_sequence_length))
        # Ignore weight if it is a sequence feature.
        weight = array_ops.ones_like(inp, dtype=dtypes.float32)
    elif feature.output_shape:
        # Eagerly run the following op as the result as to be a number in
        # order to use it as part of the output shape.
        with ops.init_scope():
            output_batch_size = math_ops.reduce_prod(feature.output_shape).numpy()
        # If the output batch size matches the data batch size, treat it as
        # normal ragged input.
        if output_batch_size == batch_size:
            inp, weight = inp.to_tensor(), weight.to_tensor()
        # If the data batch size is a factor of the output batch size, the
        # divide result will be the sequence length. Ignore the weights and
        # combiner.
        elif output_batch_size > batch_size and output_batch_size % batch_size == 0:
            # Pad or truncate in the sequence dimension
            seq_length = output_batch_size // batch_size
            inp = inp.to_tensor(shape=(batch_size, seq_length))
            # Ignore weight if it is a sequence feature.
            weight = array_ops.ones_like(inp, dtype=dtypes.float32)
        else:
            raise ValueError(
                "Output shape set in the FeatureConfig should be the factor of "
                "the input data batch size. But instead got output shape {}, "
                "input data batch size {}".format(feature.output_shape,
                                                  batch_size))
    else:
        inp, weight = inp.to_tensor(), weight.to_tensor()
    exit((inp, weight))

inp, weight = tpu.outside_compilation(
    ragged_to_dense_outside_compilation,
    inp=inp,
    weight=weight,
    batch_size=batch_size,
    feature=feature)

embeddings = embedding_ops.embedding_lookup_v2(table, inp)
weight = array_ops.expand_dims(weight, -1)
embeddings *= weight

if feature.output_shape:
    with ops.init_scope():
        output_batch_size = math_ops.reduce_prod(feature.output_shape).numpy()
    if output_batch_size == batch_size:
        embeddings = self._apply_combiner_to_embeddings(embeddings, weight,
                                                        feature.table.combiner)
    embeddings = array_ops.reshape(
        embeddings, shape=feature.output_shape + [feature.table.dim])
else:
    if feature.max_sequence_length == 0:
        embeddings = self._apply_combiner_to_embeddings(embeddings, weight,
                                                        feature.table.combiner)
exit(embeddings)
