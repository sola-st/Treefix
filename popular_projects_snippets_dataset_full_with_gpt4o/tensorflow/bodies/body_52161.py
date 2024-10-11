# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
column = fc._weighted_categorical_column(
    categorical_column=fc._categorical_column_with_identity(
        key='ids', num_buckets=3),
    weight_feature_key='values')
with ops.Graph().as_default():
    with self.assertRaisesRegex(ValueError,
                                r'Dimensions.*are not compatible'):
        fc.linear_model({
            'ids': sparse_tensor.SparseTensorValue(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(0, 2, 1),
                dense_shape=(2, 2)),
            'values': sparse_tensor.SparseTensorValue(
                indices=((0, 0), (0, 1), (1, 0), (1, 1)),
                values=(.5, 11., 1., .1),
                dense_shape=(2, 2))
        }, (column,))
