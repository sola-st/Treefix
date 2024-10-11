# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Private method that follows the signature of _get_dense_tensor."""
# This method is called from a variable_scope with name _var_scope_name,
# which is shared among all shared embeddings. Open a name_scope here, so
# that the ops for different columns have distinct names.
with ops.name_scope(None, default_name=self.name):
    # Get sparse IDs and weights.
    sparse_tensors = self.categorical_column.get_sparse_tensors(
        transformation_cache, state_manager)
    sparse_ids = sparse_tensors.id_tensor
    sparse_weights = sparse_tensors.weight_tensor

    embedding_weights = self.shared_embedding_column_creator.embedding_weights

    sparse_id_rank = tensor_shape.dimension_value(
        sparse_ids.dense_shape.get_shape()[0])
    embedding_lookup_sparse = embedding_ops.safe_embedding_lookup_sparse
    if (not self.use_safe_embedding_lookup and sparse_id_rank is not None and
        sparse_id_rank <= 2):
        embedding_lookup_sparse = embedding_ops.embedding_lookup_sparse_v2
    # Return embedding lookup result.
    exit(embedding_lookup_sparse(
        embedding_weights,
        sparse_ids,
        sparse_weights,
        combiner=self.combiner,
        name='%s_weights' % self.name,
        max_norm=self.max_norm))
