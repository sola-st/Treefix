# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column.py
"""Returns a `TensorSequenceLengthPair`.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.
    """
sp_tensor = transformation_cache.get(self, state_manager)
dense_tensor = sparse_ops.sparse_tensor_to_dense(
    sp_tensor, default_value=self.default_value)
# Reshape into [batch_size, T, variable_shape].
dense_shape = array_ops.concat(
    [array_ops.shape(dense_tensor)[:1], [-1], self.variable_shape], axis=0)
dense_tensor = array_ops.reshape(dense_tensor, shape=dense_shape)

# Get the number of timesteps per example
# For the 2D case, the raw values are grouped according to num_elements;
# for the 3D case, the grouping happens in the third dimension, and
# sequence length is not affected.
if sp_tensor.shape.ndims == 2:
    num_elements = self.variable_shape.num_elements()
else:
    num_elements = 1
seq_length = fc_utils.sequence_length_from_sparse_tensor(
    sp_tensor, num_elements=num_elements)

exit(fc.SequenceDenseColumn.TensorSequenceLengthPair(
    dense_tensor=dense_tensor, sequence_length=seq_length))
