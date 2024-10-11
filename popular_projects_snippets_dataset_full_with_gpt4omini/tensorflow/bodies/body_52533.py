# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# Provide three _DenseColumn's to input_layer: a _NumericColumn, a
# _BucketizedColumn, and an _EmbeddingColumn.  Only the _EmbeddingColumn
# creates a Variable.
apple_numeric_column = fc.numeric_column('apple_numeric_column')
banana_dense_feature = fc.numeric_column('banana_dense_feature')
banana_dense_feature_bucketized = fc.bucketized_column(
    banana_dense_feature, boundaries=[0.])
cherry_sparse_column = fc.categorical_column_with_hash_bucket(
    'cherry_sparse_feature', hash_bucket_size=5)
dragonfruit_embedding_column = fc.embedding_column(
    cherry_sparse_column, dimension=10)
with ops.Graph().as_default():
    features = {
        'apple_numeric_column': [[3.], [4.]],
        'banana_dense_feature': [[-1.], [4.]],
        'cherry_sparse_feature': [['a'], ['x']],
    }
    cols_to_output_tensors = {}
    all_cols = [
        apple_numeric_column, banana_dense_feature_bucketized,
        dragonfruit_embedding_column
    ]
    input_layer = fc_old.input_layer(
        features, all_cols, cols_to_output_tensors=cols_to_output_tensors)

    # We check the mapping by checking that we have the right keys,
    # and that the values (output_tensors) were indeed the ones used to
    # form the input layer.
    self.assertCountEqual(all_cols, cols_to_output_tensors.keys())
    input_layer_inputs = [tensor for tensor in input_layer.op.inputs[:-1]]
    output_tensors = [tensor for tensor in cols_to_output_tensors.values()]
    self.assertCountEqual(input_layer_inputs, output_tensors)
