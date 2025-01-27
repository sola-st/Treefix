# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    column = fc._categorical_column_with_vocabulary_file(
        key='aaa',
        vocabulary_file=self._wire_vocabulary_file_name,
        vocabulary_size=self._wire_vocabulary_size + 1)
    inputs = sparse_tensor.SparseTensorValue(
        indices=((0, 0), (1, 0), (1, 1)),
        values=('marlo', 'skywalker', 'omar'),
        dense_shape=(2, 2))
    column._get_sparse_tensors(_LazyBuilder({'aaa': inputs}))
    with self.assertRaisesRegex(errors.OpError, 'Invalid vocab_size'):
        with self.cached_session():
            lookup_ops.tables_initializer().run()
