# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns a SparseTensor with identity values."""
if not input_tensor.dtype.is_integer:
    raise ValueError('Invalid input, not integer. key: {} dtype: {}'.format(
        self.key, input_tensor.dtype))
values = input_tensor.values
if input_tensor.values.dtype != dtypes.int64:
    values = math_ops.cast(values, dtypes.int64, name='values')
if self.default_value is not None:
    values = math_ops.cast(input_tensor.values, dtypes.int64, name='values')
    num_buckets = math_ops.cast(
        self.num_buckets, dtypes.int64, name='num_buckets')
    zero = math_ops.cast(0, dtypes.int64, name='zero')
    # Assign default for out-of-range values.
    values = array_ops.where_v2(
        math_ops.logical_or(
            values < zero, values >= num_buckets, name='out_of_range'),
        array_ops.fill(
            dims=array_ops.shape(values),
            value=math_ops.cast(self.default_value, dtypes.int64),
            name='default_values'), values)

exit(sparse_tensor_lib.SparseTensor(
    indices=input_tensor.indices,
    values=values,
    dense_shape=input_tensor.dense_shape))
