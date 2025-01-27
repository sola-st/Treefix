# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    column = fc._categorical_column_with_identity(key='aaa', num_buckets=3)
    inputs = sparse_tensor.SparseTensorValue(
        indices=((0, 0), (1, 0), (1, 1)),
        values=(0, 1, 0),
        dense_shape=(2, 2))
    id_weight_pair = column._get_sparse_tensors(_LazyBuilder({'aaa': inputs}))
    self.assertIsNone(id_weight_pair.weight_tensor)
    with _initialized_session():
        _assert_sparse_tensor_value(
            self,
            sparse_tensor.SparseTensorValue(
                indices=inputs.indices,
                values=np.array((0, 1, 0), dtype=np.int64),
                dense_shape=inputs.dense_shape),
            id_weight_pair.id_tensor.eval())
