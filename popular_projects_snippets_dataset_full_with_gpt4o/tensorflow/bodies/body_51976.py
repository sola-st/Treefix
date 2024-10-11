# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
# Provide three _DenseColumn's to input_layer: a _NumericColumn, a
# _BucketizedColumn, and an _EmbeddingColumn.  Only the _EmbeddingColumn
# creates a Variable.
price1 = fc._numeric_column('price1')
dense_feature = fc._numeric_column('dense_feature')
dense_feature_bucketized = fc._bucketized_column(
    dense_feature, boundaries=[0.])
some_sparse_column = fc._categorical_column_with_hash_bucket(
    'sparse_feature', hash_bucket_size=5)
some_embedding_column = fc._embedding_column(
    some_sparse_column, dimension=10)
with ops.Graph().as_default():
    features = {
        'price1': [[3.], [4.]],
        'dense_feature': [[-1.], [4.]],
        'sparse_feature': [['a'], ['x']],
    }
    cols_to_vars = {}
    all_cols = [price1, dense_feature_bucketized, some_embedding_column]
    fc.input_layer(features, all_cols, cols_to_vars=cols_to_vars)
    self.assertCountEqual(list(cols_to_vars.keys()), all_cols)
    self.assertEqual(0, len(cols_to_vars[price1]))
    self.assertEqual(0, len(cols_to_vars[dense_feature_bucketized]))
    self.assertEqual(1, len(cols_to_vars[some_embedding_column]))
    self.assertIsInstance(cols_to_vars[some_embedding_column][0],
                          variables_lib.Variable)
    self.assertAllEqual(cols_to_vars[some_embedding_column][0].shape, [5, 10])
