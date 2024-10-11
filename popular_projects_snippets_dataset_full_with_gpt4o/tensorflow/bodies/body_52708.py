# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
categorical_column = fc.categorical_column_with_identity(
    key='aaa', num_buckets=3)
embedding_dimension = 2
embedding_column = fc.embedding_column(
    categorical_column, dimension=embedding_dimension)
self.assertIs(categorical_column, embedding_column.categorical_column)
self.assertEqual(embedding_dimension, embedding_column.dimension)
self.assertEqual('mean', embedding_column.combiner)
self.assertIsNone(embedding_column.ckpt_to_load_from)
self.assertIsNone(embedding_column.tensor_name_in_ckpt)
self.assertIsNone(embedding_column.max_norm)
self.assertTrue(embedding_column.trainable)
self.assertEqual('aaa_embedding', embedding_column.name)
self.assertEqual((embedding_dimension,), embedding_column.variable_shape)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.int64)
}, embedding_column.parse_example_spec)
self.assertTrue(embedding_column._is_v2_column)
