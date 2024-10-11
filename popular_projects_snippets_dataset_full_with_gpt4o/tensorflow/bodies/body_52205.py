# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
self._embedding_weight_var = self.add_variable(
    name='embedding_weights',
    shape=self._embedding_shape,
    dtype=dtypes.float32,
    initializer=self._initializer,
    trainable=self.trainable)
if self._weight_collections and not context.executing_eagerly():
    _add_to_collections(self._embedding_weight_var, self._weight_collections)
self.built = True
