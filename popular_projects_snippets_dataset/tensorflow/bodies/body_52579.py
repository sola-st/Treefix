# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
some_sparse_column = fc.categorical_column_with_hash_bucket(
    'sparse_feature', hash_bucket_size=5)
some_embedding_column = fc.embedding_column(
    some_sparse_column, dimension=10)

with ops.Graph().as_default():
    features = {
        'sparse_feature': [['a'], ['x']],
    }
    all_cols = [some_embedding_column]
    fc_old.input_layer(features, all_cols)
    fc_old.input_layer(features, all_cols)
    # Make sure that 2 variables get created in this case.
    self.assertEqual(2, len(
        ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)))
    expected_var_names = [
        'input_layer/sparse_feature_embedding/embedding_weights:0',
        'input_layer_1/sparse_feature_embedding/embedding_weights:0'
    ]
    self.assertCountEqual(
        expected_var_names,
        [v.name for v in ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)])
