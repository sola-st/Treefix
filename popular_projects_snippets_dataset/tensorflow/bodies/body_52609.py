# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_vocabulary_file(
    key='aaa',
    vocabulary_file=self._wire_vocabulary_file_name,
    vocabulary_size=self._wire_vocabulary_size + 1)
inputs = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1)),
    values=('marlo', 'skywalker', 'omar'),
    dense_shape=(2, 2))
with self.assertRaisesRegex(*self._VOCABULARY_SIZE_ERROR):
    column.get_sparse_tensors(
        fc.FeatureTransformationCache({
            'aaa': inputs
        }), None)
    self.evaluate(lookup_ops.tables_initializer())
