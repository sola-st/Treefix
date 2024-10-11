# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
"""Embedding lookup for sparse tensor based on its feature config.

    Args:
      inp: a single SparseTensor input.
      weight: None or SparseTensor which has the same shape of the input.
      table: a table variable.
      feature: a feature config.

    Returns:
      Embedding lookup result.
    """

# This computation needs to placed outside of tpu as the size of the
# indices and values can change for different batch which can cause
# the program to re-compile.
def sparse_to_dense_computation(inp, weight):
    if weight is None:
        weight = sparse_tensor.SparseTensor(
            inp.indices,
            array_ops.ones_like(inp.values, dtype=dtypes.float32),
            dense_shape=inp.dense_shape)
    # Pad the sparse tensor to be dense tensor.
    inp = sparse_ops.sparse_tensor_to_dense(inp)
    weight = sparse_ops.sparse_tensor_to_dense(weight)
    exit((inp, weight))

inp, weight = tpu.outside_compilation(
    sparse_to_dense_computation, inp=inp, weight=weight)

embeddings = embedding_ops.embedding_lookup_v2(table, inp)
weight = array_ops.expand_dims(weight, -1)
embeddings *= weight
if not feature.output_shape and feature.max_sequence_length > 0:
    embeddings = self._pad_or_truncate_with_sequence_length(
        embeddings, feature.max_sequence_length)
else:
    embeddings = self._apply_combiner_to_embeddings(embeddings, weight,
                                                    feature.table.combiner)
exit(embeddings)
