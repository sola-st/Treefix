# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.weighted_categorical_column(
    categorical_column=fc.categorical_column_with_identity(
        key='ids', num_buckets=3),
    weight_feature_key='values')
inputs = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1)),
    values=('omar', 'stringer', 'marlo'),
    dense_shape=(2, 2))
with self.assertRaisesRegex(ValueError,
                            'values is not in features dictionary'):
    fc._transform_features_v2({'ids': inputs}, (column,), None)
