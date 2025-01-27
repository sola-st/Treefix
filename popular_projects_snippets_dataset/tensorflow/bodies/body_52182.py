# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
self._bias_variable = self.add_variable(
    'bias_weights',
    shape=[self._units],
    initializer=init_ops.zeros_initializer(),
    trainable=self.trainable)
_add_to_collections(self._bias_variable, self._weight_collections)
self.built = True
