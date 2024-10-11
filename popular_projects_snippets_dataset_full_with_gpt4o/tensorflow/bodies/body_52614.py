# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_vocabulary_file(
    key='aaa',
    vocabulary_file=self._warriors_vocabulary_file_name,
    vocabulary_size=self._warriors_vocabulary_size,
    dtype=dtypes.int32)
inputs = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1)),
    values=('omar', 'stringer', 'marlo'),
    dense_shape=(2, 2))
with self.assertRaisesRegex(ValueError, 'dtype must be compatible'):
    column.get_sparse_tensors(
        fc.FeatureTransformationCache({
            'aaa': inputs
        }), None)
