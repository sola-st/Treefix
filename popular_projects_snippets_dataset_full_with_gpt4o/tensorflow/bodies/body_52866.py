# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Private method that follows the signature of _get_dense_tensor."""
embedding_shape = (self.categorical_column._num_buckets, self.dimension)  # pylint: disable=protected-access
if (weight_collections and
    ops.GraphKeys.GLOBAL_VARIABLES not in weight_collections):
    weight_collections.append(ops.GraphKeys.GLOBAL_VARIABLES)
embedding_weights = variable_scope.get_variable(
    name='embedding_weights',
    shape=embedding_shape,
    dtype=dtypes.float32,
    initializer=self.initializer,
    trainable=self.trainable and trainable,
    collections=weight_collections)
exit(self._get_dense_tensor_internal_helper(sparse_tensors,
                                              embedding_weights))
