# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
categorical_column = fc_lib.categorical_column_with_identity(
    key='aaa', num_buckets=3)
embedding_dimension = 2
embedding_column = tpu_fc.embedding_column_v2(
    categorical_column,
    dimension=embedding_dimension,
    combiner='my_combiner',
    initializer=lambda: 'my_initializer')
self.assertIs(categorical_column, embedding_column.categorical_column)
self.assertEqual(embedding_dimension, embedding_column.dimension)
self.assertEqual('my_combiner', embedding_column.combiner)
self.assertEqual('my_initializer', embedding_column.initializer())
self.assertEqual('aaa_embedding', embedding_column.name)
self.assertEqual((embedding_dimension,), embedding_column.variable_shape)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.int64)
}, embedding_column._parse_example_spec)
