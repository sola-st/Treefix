# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Private method that follows the signature of _get_dense_tensor."""
# This method is called from a variable_scope with name _var_scope_name,
# which is shared among all shared embeddings. Open a name_scope here, so
# that the ops for different columns have distinct names.
with ops.name_scope(None, default_name=self.name):
    # Get sparse IDs and weights.
    sparse_tensors = self.categorical_column._get_sparse_tensors(  # pylint: disable=protected-access
        inputs,
        weight_collections=weight_collections,
        trainable=trainable)
    sparse_ids = sparse_tensors.id_tensor
    sparse_weights = sparse_tensors.weight_tensor

    embedding_shape = (self.categorical_column._num_buckets, self.dimension)  # pylint: disable=protected-access
    shared_embedding_collection = ops.get_collection(
        self.shared_embedding_collection_name)
    if shared_embedding_collection:
        if len(shared_embedding_collection) > 1:
            raise ValueError(
                'Collection {} can only contain one variable. '
                'Suggested fix A: Choose a unique name for this collection. '
                'Suggested fix B: Do not add any variables to this collection. '
                'The feature_column library already adds a variable under the '
                'hood.'.format(shared_embedding_collection))
        embedding_weights = shared_embedding_collection[0]
        if embedding_weights.get_shape() != embedding_shape:
            raise ValueError(
                'Shared embedding collection {} contains variable {} of '
                'unexpected shape {}. Expected shape is {}. '
                'Suggested fix A: Choose a unique name for this collection. '
                'Suggested fix B: Do not add any variables to this collection. '
                'The feature_column library already adds a variable under the '
                'hood.'.format(self.shared_embedding_collection_name,
                               embedding_weights.name,
                               embedding_weights.get_shape(), embedding_shape))
    else:
        embedding_weights = variable_scope.get_variable(
            name='embedding_weights',
            shape=embedding_shape,
            dtype=dtypes.float32,
            initializer=self.initializer,
            trainable=self.trainable and trainable,
            collections=weight_collections)
        ops.add_to_collection(self.shared_embedding_collection_name,
                              embedding_weights)
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
