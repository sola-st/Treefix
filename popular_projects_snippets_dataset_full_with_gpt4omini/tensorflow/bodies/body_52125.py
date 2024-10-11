# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    categorical_column_a = fc._categorical_column_with_identity(
        key='aaa', num_buckets=3)
    categorical_column_b = fc._categorical_column_with_identity(
        key='bbb', num_buckets=3)
    embedding_dimension = 2
    original_a, _ = fc_new.shared_embedding_columns(
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
        self.assertEqual(3, embedding_column_a.categorical_column._num_buckets)
        self.assertEqual(
            {'aaa': parsing_ops.VarLenFeature(dtypes.int64)},
            embedding_column_a.categorical_column._parse_example_spec)

        self.assertEqual(embedding_dimension, embedding_column_a.dimension)
        self.assertEqual('my_combiner', embedding_column_a.combiner)
        self.assertEqual('shared_embedding_collection_name',
                         embedding_column_a.shared_embedding_collection_name)
        self.assertEqual('my_ckpt', embedding_column_a.ckpt_to_load_from)
        self.assertEqual('my_ckpt_tensor',
                         embedding_column_a.tensor_name_in_ckpt)
        self.assertEqual(42., embedding_column_a.max_norm)
        self.assertFalse(embedding_column_a.trainable)
        self.assertEqual('aaa_shared_embedding', embedding_column_a.name)
        self.assertEqual((embedding_dimension,),
                         embedding_column_a._variable_shape)
        self.assertEqual({'aaa': parsing_ops.VarLenFeature(dtypes.int64)},
                         embedding_column_a._parse_example_spec)
