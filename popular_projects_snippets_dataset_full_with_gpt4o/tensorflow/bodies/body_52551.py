# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# SharedEmbeddingColumns are graph-only
with ops.Graph().as_default():
    price = fc.numeric_column('price')  # v2
    some_sparse_column = fc.categorical_column_with_hash_bucket(
        'sparse_feature', hash_bucket_size=5)  # v1
    some_embedding_column = fc.embedding_column(
        some_sparse_column, dimension=10)  # v1
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=3)  # v2
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=3)  # v2
    shared_embedding_a, shared_embedding_b = fc.shared_embedding_columns(
        [categorical_column_a, categorical_column_b], dimension=2)  # v1
    all_cols = [
        price, some_embedding_column, shared_embedding_a, shared_embedding_b
    ]

    features = {
        'price': [[3.], [4.]],
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
    fc_old.linear_model(features, all_cols)
    bias = get_linear_model_bias()

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllClose([0.], self.evaluate(bias))
