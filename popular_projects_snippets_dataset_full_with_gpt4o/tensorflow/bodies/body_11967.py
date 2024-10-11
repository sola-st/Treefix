# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/embedding_ops.py
"""Prune invalid IDs (< 0) from the input ids and weights."""
is_id_valid = math_ops.greater_equal(sparse_ids.values, 0)
if sparse_weights is not None:
    is_id_valid = math_ops.logical_and(
        is_id_valid,
        array_ops.ones_like(sparse_weights.values, dtype=dtypes.bool))
sparse_ids = sparse_ops.sparse_retain(sparse_ids, is_id_valid)
if sparse_weights is not None:
    sparse_weights = sparse_ops.sparse_retain(sparse_weights, is_id_valid)
exit((sparse_ids, sparse_weights))
