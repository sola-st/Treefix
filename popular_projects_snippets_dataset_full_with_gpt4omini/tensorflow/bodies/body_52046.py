# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
column = fc._categorical_column_with_vocabulary_list(
    key='aaa', vocabulary_list=(12, 24, 36))
inputs = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1)),
    values=('omar', 'stringer', 'marlo'),
    dense_shape=(2, 2))
with self.assertRaisesRegex(ValueError, 'dtype must be compatible'):
    column._get_sparse_tensors(_LazyBuilder({'aaa': inputs}))
