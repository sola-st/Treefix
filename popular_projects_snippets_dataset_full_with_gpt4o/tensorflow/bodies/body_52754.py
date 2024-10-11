# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.weighted_categorical_column(
    categorical_column=fc.categorical_column_with_identity(
        key='ids', num_buckets=3),
    weight_feature_key='values')
strings = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1)),
    values=('omar', 'stringer', 'marlo'),
    dense_shape=(2, 2))
with self.assertRaisesRegex(ValueError, 'Bad dtype'):
    fc._transform_features_v2({
        'ids': strings,
        'values': strings
    }, (column,), None)
