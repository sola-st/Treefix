# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    column = fc._weighted_categorical_column(
        categorical_column=fc._categorical_column_with_identity(
            key='ids', num_buckets=3),
        weight_feature_key='values')
    weights = sparse_tensor.SparseTensorValue(
        indices=((0, 0), (1, 0), (1, 1)),
        values=(0.5, 1.0, 0.1),
        dense_shape=(2, 2))
    id_tensor, weight_tensor = _transform_features({
        'ids': ((0, -1), (1, 0)),
        'values': weights,
    }, (column,))[column]
    with _initialized_session():
        _assert_sparse_tensor_value(
            self,
            sparse_tensor.SparseTensorValue(
                indices=((0, 0), (1, 0), (1, 1)),
                values=np.array((0, 1, 0), dtype=np.int64),
                dense_shape=(2, 2)), self.evaluate(id_tensor))
        _assert_sparse_tensor_value(
            self,
            sparse_tensor.SparseTensorValue(
                indices=weights.indices,
                values=np.array(weights.values, dtype=np.float32),
                dense_shape=weights.dense_shape), self.evaluate(weight_tensor))
