# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    column = fc._categorical_column_with_identity(
        key='aaa', num_buckets=4, default_value=3)
    input_indices = array_ops.placeholder(dtype=dtypes.int64)
    input_values = array_ops.placeholder(dtype=dtypes.int32)
    input_shape = array_ops.placeholder(dtype=dtypes.int64)
    inputs = sparse_tensor.SparseTensorValue(
        indices=input_indices,
        values=input_values,
        dense_shape=input_shape)
    id_weight_pair = column._get_sparse_tensors(_LazyBuilder({'aaa': inputs}))
    self.assertIsNone(id_weight_pair.weight_tensor)
    with _initialized_session():
        _assert_sparse_tensor_value(
            self,
            sparse_tensor.SparseTensorValue(
                indices=np.array(((0, 0), (1, 0), (1, 1)), dtype=np.int64),
                values=np.array((1, 3, 3), dtype=np.int64),
                dense_shape=np.array((2, 2), dtype=np.int64)),
            id_weight_pair.id_tensor.eval(feed_dict={
                input_indices: ((0, 0), (1, 0), (1, 1)),
                input_values: (1, -1, 99),
                input_shape: (2, 2),
            }))
