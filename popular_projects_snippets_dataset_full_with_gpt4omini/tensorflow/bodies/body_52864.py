# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
sparse_ids = sparse_tensors.id_tensor
sparse_weights = sparse_tensors.weight_tensor

if self.ckpt_to_load_from is not None:
    to_restore = embedding_weights
    if isinstance(to_restore, variables.PartitionedVariable):
        to_restore = to_restore._get_variable_list()  # pylint: disable=protected-access
    checkpoint_utils.init_from_checkpoint(
        self.ckpt_to_load_from, {self.tensor_name_in_ckpt: to_restore})

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
