# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# SharedEmbeddingColumns are graph-only
with ops.Graph().as_default():
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=3)
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=3)
    embedding_dimension = 2
    original_a, _ = fc.shared_embedding_columns_v2(
        [categorical_column_a, categorical_column_b],
        dimension=embedding_dimension,
        combiner='my_combiner',
        initializer=lambda: 'my_initializer',
        shared_embedding_collection_name='shared_embedding_collection_name',
        ckpt_to_load_from='my_ckpt',
        tensor_name_in_ckpt='my_ckpt_tensor',
        max_norm=42.,
        trainable=False)
    for embedding_column_a in (original_a, copy.deepcopy(original_a)):
        self.assertEqual('aaa', embedding_column_a.categorical_column.name)
        self.assertEqual(3, embedding_column_a.categorical_column.num_buckets)
        self.assertEqual({
            'aaa': parsing_ops.VarLenFeature(dtypes.int64)
        }, embedding_column_a.categorical_column.parse_example_spec)

        self.assertEqual(42., embedding_column_a.max_norm)
        self.assertEqual('aaa_shared_embedding', embedding_column_a.name)
        self.assertEqual((embedding_dimension,),
                         embedding_column_a.variable_shape)
        self.assertEqual({
            'aaa': parsing_ops.VarLenFeature(dtypes.int64)
        }, embedding_column_a.parse_example_spec)
