# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    categorical_column_a = fc._categorical_column_with_identity(
        key='aaa', num_buckets=3)
    categorical_column_b = fc._categorical_column_with_identity(
        key='bbb', num_buckets=3)
    embedding_dimension = 2
    embedding_column_b, embedding_column_a = fc_new.shared_embedding_columns(
        [categorical_column_b, categorical_column_a],
        dimension=embedding_dimension)
    self.assertIs(categorical_column_a, embedding_column_a.categorical_column)
    self.assertIs(categorical_column_b, embedding_column_b.categorical_column)
    self.assertEqual(embedding_dimension, embedding_column_a.dimension)
    self.assertEqual(embedding_dimension, embedding_column_b.dimension)
    self.assertEqual('mean', embedding_column_a.combiner)
    self.assertEqual('mean', embedding_column_b.combiner)
    self.assertIsNone(embedding_column_a.ckpt_to_load_from)
    self.assertIsNone(embedding_column_b.ckpt_to_load_from)
    self.assertEqual('aaa_bbb_shared_embedding',
                     embedding_column_a.shared_embedding_collection_name)
    self.assertEqual('aaa_bbb_shared_embedding',
                     embedding_column_b.shared_embedding_collection_name)
    self.assertIsNone(embedding_column_a.tensor_name_in_ckpt)
    self.assertIsNone(embedding_column_b.tensor_name_in_ckpt)
    self.assertIsNone(embedding_column_a.max_norm)
    self.assertIsNone(embedding_column_b.max_norm)
    self.assertTrue(embedding_column_a.trainable)
    self.assertTrue(embedding_column_b.trainable)
    self.assertEqual('aaa_shared_embedding', embedding_column_a.name)
    self.assertEqual('bbb_shared_embedding', embedding_column_b.name)
    self.assertEqual('aaa_bbb_shared_embedding',
                     embedding_column_a._var_scope_name)
    self.assertEqual('aaa_bbb_shared_embedding',
                     embedding_column_b._var_scope_name)
    self.assertEqual((embedding_dimension,),
                     embedding_column_a._variable_shape)
    self.assertEqual((embedding_dimension,),
                     embedding_column_b._variable_shape)
    self.assertEqual({'aaa': parsing_ops.VarLenFeature(dtypes.int64)},
                     embedding_column_a._parse_example_spec)
    self.assertEqual({'bbb': parsing_ops.VarLenFeature(dtypes.int64)},
                     embedding_column_b._parse_example_spec)
