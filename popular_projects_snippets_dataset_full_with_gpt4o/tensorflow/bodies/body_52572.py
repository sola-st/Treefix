# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price1 = fc.numeric_column('price1')
dense_feature = fc.numeric_column('dense_feature')
dense_feature_bucketized = fc.bucketized_column(
    dense_feature, boundaries=[0.])
some_sparse_column = fc.categorical_column_with_hash_bucket(
    'sparse_feature', hash_bucket_size=5)
some_embedding_column = fc.embedding_column(
    some_sparse_column, dimension=10)
with ops.Graph().as_default():
    features = {
        'price1': [[3.], [4.]],
        'dense_feature': [[-1.], [4.]],
        'sparse_feature': [['a'], ['x']],
    }
    cols_to_vars = {}
    all_cols = [price1, dense_feature_bucketized, some_embedding_column]
    with variable_scope.variable_scope(
        'input_from_feature_columns',
        partitioner=partitioned_variables.fixed_size_partitioner(3, axis=0)):
        fc_old.input_layer(features, all_cols, cols_to_vars=cols_to_vars)
    self.assertCountEqual(list(cols_to_vars.keys()), all_cols)
    self.assertEqual(0, len(cols_to_vars[price1]))
    self.assertEqual(0, len(cols_to_vars[dense_feature_bucketized]))
    self.assertEqual(3, len(cols_to_vars[some_embedding_column]))
    self.assertEqual(
        'input_from_feature_columns/input_layer/sparse_feature_embedding/'
        'embedding_weights/part_0:0',
        cols_to_vars[some_embedding_column][0].name)
    self.assertAllEqual(cols_to_vars[some_embedding_column][0].shape, [2, 10])
    self.assertAllEqual(cols_to_vars[some_embedding_column][1].shape, [2, 10])
    self.assertAllEqual(cols_to_vars[some_embedding_column][2].shape, [1, 10])
