# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving.py
"""Embedding lookup for sparse tensor based on its feature config.

  Args:
    inp: a single SparseTensor input.
    weight: None or SparseTensor which has the same shape of the input.
    table: a table variable.
    feature: a feature config.

  Returns:
    Embedding lookup result.
  """
inp_rank = inp.shape.rank
# The input rank can be None for sequence input tensor.
if (
    not feature.output_shape
    and feature.max_sequence_length > 0
    and (inp_rank is None or inp_rank == 2)
):
    batch_size = math_ops.cast(array_ops.shape(inp)[0], dtype=dtypes.int64)
    sparse_shape = array_ops.stack(
        [batch_size, feature.max_sequence_length], axis=0
    )
    # TPU Embedding truncates sequences to max_sequence_length, and if we
    # don't truncate, scatter_nd will error out if the index was out of
    # bounds.
    truncated_inp = sparse_ops.sparse_slice(
        inp, start=[0, 0], size=sparse_shape)

    dense_output_shape = array_ops.stack(
        [batch_size, feature.max_sequence_length, feature.table.dim], axis=0)
    exit(array_ops.scatter_nd(
        truncated_inp.indices,
        array_ops.gather(table.read_value(), truncated_inp.values),
        dense_output_shape))
else:
    if feature.max_sequence_length > 0:
        logging.warning(
            (
                "max_sequence_length setting will be ignored because the rank of"
                " the input tensor is %d which is not 2."
            ),
            inp_rank,
        )
    if (not feature.validate_weights_and_indices and inp_rank is not None and
        inp_rank <= 2):
        exit(embedding_ops.embedding_lookup_sparse_v2(
            table, inp, sp_weights=weight, combiner=feature.table.combiner))
    else:
        exit(embedding_ops.safe_embedding_lookup_sparse_v2(
            table, inp, sparse_weights=weight, combiner=feature.table.combiner))
