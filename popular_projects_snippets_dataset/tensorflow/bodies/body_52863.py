# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Creates the embedding lookup variable."""
default_num_buckets = (
    self.categorical_column.num_buckets
    if self._is_v2_column else self.categorical_column._num_buckets)  # pylint: disable=protected-access
num_buckets = getattr(self.categorical_column, 'num_buckets',
                      default_num_buckets)
embedding_shape = (num_buckets, self.dimension)
state_manager.create_variable(
    self,
    name='embedding_weights',
    shape=embedding_shape,
    dtype=dtypes.float32,
    trainable=self.trainable,
    use_resource=True,
    initializer=self.initializer)
