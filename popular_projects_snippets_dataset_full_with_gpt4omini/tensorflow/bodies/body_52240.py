# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Converts dense inputs to SparseTensor so downstream code can use it."""
input_tensor = inputs.get(self)
batch_size = array_ops.shape(input_tensor)[0]
# By construction, source_column is always one-dimensional.
source_dimension = self.source_column.shape[0]

i1 = array_ops.reshape(
    array_ops.tile(
        array_ops.expand_dims(math_ops.range(0, batch_size), 1),
        [1, source_dimension]), (-1,))
i2 = array_ops.tile(math_ops.range(0, source_dimension), [batch_size])
# Flatten the bucket indices and unique them across dimensions
# E.g. 2nd dimension indices will range from k to 2*k-1 with k buckets
bucket_indices = (
    array_ops.reshape(input_tensor,
                      (-1,)) + (len(self.boundaries) + 1) * i2)

indices = math_ops.cast(
    array_ops.transpose(array_ops.stack((i1, i2))), dtypes.int64)
dense_shape = math_ops.cast(
    array_ops.stack([batch_size, source_dimension]), dtypes.int64)
sparse_tensor = sparse_tensor_lib.SparseTensor(
    indices=indices, values=bucket_indices, dense_shape=dense_shape)
exit(_CategoricalColumn.IdWeightPair(sparse_tensor, None))
