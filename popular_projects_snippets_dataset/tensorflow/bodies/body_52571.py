# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# Provide 5 DenseColumn's to input_layer: a NumericColumn, a
# BucketizedColumn, an EmbeddingColumn, two SharedEmbeddingColumns. The
# EmbeddingColumn creates a Variable and the two SharedEmbeddingColumns
# shared one variable.
# SharedEmbeddingColumns are graph-only
with ops.Graph().as_default():
    price1 = fc.numeric_column('price1')
    dense_feature = fc.numeric_column('dense_feature')
    dense_feature_bucketized = fc.bucketized_column(
        dense_feature, boundaries=[0.])
    some_sparse_column = fc.categorical_column_with_hash_bucket(
        'sparse_feature', hash_bucket_size=5)
    some_embedding_column = fc.embedding_column(
        some_sparse_column, dimension=10)
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=3)
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=3)
    shared_embedding_a, shared_embedding_b = fc.shared_embedding_columns(
        [categorical_column_a, categorical_column_b], dimension=2)
    features = {
        'price1': [[3.], [4.]],
        'dense_feature': [[-1.], [4.]],
        'sparse_feature': [['a'], ['x']],
        'aaa':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(0, 1, 0),
                dense_shape=(2, 2)),
        'bbb':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(1, 2, 1),
                dense_shape=(2, 2)),
    }
    cols_to_vars = {}
    all_cols = [
        price1, dense_feature_bucketized, some_embedding_column,
        shared_embedding_a, shared_embedding_b
    ]
    fc_old.input_layer(features, all_cols, cols_to_vars=cols_to_vars)
    self.assertCountEqual(list(cols_to_vars.keys()), all_cols)
    self.assertEqual(0, len(cols_to_vars[price1]))
    self.assertEqual(0, len(cols_to_vars[dense_feature_bucketized]))
    self.assertEqual(1, len(cols_to_vars[some_embedding_column]))
    self.assertEqual(1, len(cols_to_vars[shared_embedding_a]))
    # This is a bug in the current implementation and should be fixed in the
    # new one.
    self.assertEqual(0, len(cols_to_vars[shared_embedding_b]))
    self.assertIsInstance(cols_to_vars[some_embedding_column][0],
                          variables_lib.Variable)
    self.assertAllEqual(cols_to_vars[some_embedding_column][0].shape, [5, 10])
    self.assertIsInstance(cols_to_vars[shared_embedding_a][0],
                          variables_lib.Variable)
    self.assertAllEqual(cols_to_vars[shared_embedding_a][0].shape, [3, 2])
