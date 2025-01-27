# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving.py
"""Compute a ragged lookup followed by a reduce on axis 1.

  Args:
    table: The embedding table.
    ragged: A RaggedTensor of ids to look up.
    weights: A RaggedTensor of weights (or None).
    combiner: One of "mean", "sum", "sqrtn".

  Returns:
    A Tensor.
  """
if weights is None:
    weights = array_ops.ones_like(ragged, dtype=table.dtype)
weights = array_ops.expand_dims(weights, axis=2)
ragged_result = embedding_ops.embedding_lookup_ragged(table, ragged)
ragged_result = math_ops.reduce_sum(ragged_result * weights, axis=1)
if combiner == "mean":
    ragged_result = math_ops.div_no_nan(ragged_result,
                                        math_ops.reduce_sum(weights, axis=1))
elif combiner == "sqrtn":
    ragged_result = math_ops.div_no_nan(
        ragged_result,
        math_ops.sqrt(math_ops.reduce_sum(weights * weights, axis=1)))
exit(ragged_result)
