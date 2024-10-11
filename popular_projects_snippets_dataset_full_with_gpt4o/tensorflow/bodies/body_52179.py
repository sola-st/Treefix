# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
if isinstance(self._feature_column, _CategoricalColumn):
    weight = self.add_variable(
        name='weights',
        shape=(self._feature_column._num_buckets, self._units),  # pylint: disable=protected-access
        initializer=init_ops.zeros_initializer(),
        trainable=self.trainable)
else:
    num_elements = self._feature_column._variable_shape.num_elements()  # pylint: disable=protected-access
    weight = self.add_variable(
        name='weights',
        shape=[num_elements, self._units],
        initializer=init_ops.zeros_initializer(),
        trainable=self.trainable)
_add_to_collections(weight, self._weight_collections)
self._weight_var = weight
self.built = True
