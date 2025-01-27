# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    column = fc._categorical_column_with_vocabulary_file(
        key='aaa', vocabulary_file='file_does_not_exist', vocabulary_size=10)
    inputs = sparse_tensor.SparseTensorValue(
        indices=((0, 0), (1, 0), (1, 1)),
        values=('marlo', 'skywalker', 'omar'),
        dense_shape=(2, 2))
    column._get_sparse_tensors(_LazyBuilder({'aaa': inputs}))
    with self.assertRaisesRegex(errors.OpError, 'file_does_not_exist'):
        with self.cached_session():
            lookup_ops.tables_initializer().run()
