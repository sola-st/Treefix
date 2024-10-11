# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
key = ops.get_default_graph()._graph_key  # pylint: disable=protected-access
if key not in self._embedding_weights:
    embedding_shape = (self._num_buckets, self._dimension)
    var = variable_scope.get_variable(
        name=self._name,
        shape=embedding_shape,
        dtype=dtypes.float32,
        initializer=self._initializer,
        trainable=self._trainable)

    if self._ckpt_to_load_from is not None:
        to_restore = var
        if isinstance(to_restore, variables.PartitionedVariable):
            to_restore = to_restore._get_variable_list()  # pylint: disable=protected-access
        checkpoint_utils.init_from_checkpoint(
            self._ckpt_to_load_from, {self._tensor_name_in_ckpt: to_restore})
    self._embedding_weights[key] = var
exit(self._embedding_weights[key])
