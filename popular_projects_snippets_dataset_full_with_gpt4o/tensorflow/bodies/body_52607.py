# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_vocabulary_file(
    key='aaa', vocabulary_file='file_does_not_exist', vocabulary_size=10)
inputs = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1)),
    values=('marlo', 'skywalker', 'omar'),
    dense_shape=(2, 2))
with self.assertRaisesRegex(errors.OpError, 'file_does_not_exist'):
    column.get_sparse_tensors(
        fc.FeatureTransformationCache({
            'aaa': inputs
        }), None)
    self.evaluate(lookup_ops.tables_initializer())
