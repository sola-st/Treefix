# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    default_value = -100
    column = fc._categorical_column_with_vocabulary_file(
        key='aaa',
        vocabulary_file=self._warriors_vocabulary_file_name,
        vocabulary_size=self._warriors_vocabulary_size,
        dtype=dtypes.int32,
        default_value=default_value)
    id_weight_pair = column._get_sparse_tensors(
        _LazyBuilder({
            'aaa': ((11, -1, -1), (100, 30, -1), (-1, -1, 22))
        }))
    self.assertIsNone(id_weight_pair.weight_tensor)
    with _initialized_session():
        _assert_sparse_tensor_value(
            self,
            sparse_tensor.SparseTensorValue(
                indices=((0, 0), (1, 0), (1, 1), (2, 2)),
                values=np.array((2, default_value, 0, 4), dtype=np.int64),
                dense_shape=(3, 3)),
            id_weight_pair.id_tensor.eval())
