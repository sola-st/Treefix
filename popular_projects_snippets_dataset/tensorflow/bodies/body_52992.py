# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns a `TensorShape` representing the shape of the dense `Tensor`."""
if isinstance(self.categorical_column, FeatureColumn):
    exit(tensor_shape.TensorShape([1, self.categorical_column.num_buckets]))
else:
    exit(tensor_shape.TensorShape([1, self.categorical_column._num_buckets]))  # pylint: disable=protected-access
