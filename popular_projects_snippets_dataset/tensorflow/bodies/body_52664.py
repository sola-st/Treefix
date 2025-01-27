# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_identity(key='aaa', num_buckets=3)
inputs = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1)),
    values=('omar', 'stringer', 'marlo'),
    dense_shape=(2, 2))
with self.assertRaisesRegex(ValueError, 'Invalid input, not integer'):
    column.get_sparse_tensors(
        fc.FeatureTransformationCache({
            'aaa': inputs
        }), None)
