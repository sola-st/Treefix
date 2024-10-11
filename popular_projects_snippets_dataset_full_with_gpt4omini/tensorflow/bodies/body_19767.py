# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_test.py
categorical_column_a = fc_lib.categorical_column_with_identity(
    key='aaa', num_buckets=3)
categorical_column_b = fc_lib.categorical_column_with_identity(
    key='bbb', num_buckets=3)
embedding_dimension = 2
embedding_column_a, embedding_column_b = tpu_fc.shared_embedding_columns(
    [categorical_column_a, categorical_column_b],
    dimension=embedding_dimension,
    combiner='my_combiner',
    initializer=lambda: 'my_initializer',
    shared_embedding_collection_name='var_scope_name')
self.assertIs(categorical_column_a, embedding_column_a.categorical_column)
self.assertIs(categorical_column_b, embedding_column_b.categorical_column)
self.assertEqual(embedding_dimension, embedding_column_a.dimension)
self.assertEqual(embedding_dimension, embedding_column_b.dimension)
self.assertEqual('my_combiner', embedding_column_a.combiner)
self.assertEqual('my_combiner', embedding_column_b.combiner)
self.assertEqual('my_initializer', embedding_column_a.initializer())
self.assertEqual('my_initializer', embedding_column_b.initializer())
self.assertEqual('var_scope_name',
                 embedding_column_a.shared_embedding_collection_name)
self.assertEqual('var_scope_name',
                 embedding_column_b.shared_embedding_collection_name)
self.assertEqual('aaa_shared_embedding', embedding_column_a.name)
self.assertEqual('bbb_shared_embedding', embedding_column_b.name)
self.assertEqual('var_scope_name', embedding_column_a._var_scope_name)
self.assertEqual('var_scope_name', embedding_column_b._var_scope_name)
self.assertEqual((embedding_dimension,), embedding_column_a._variable_shape)
self.assertEqual((embedding_dimension,), embedding_column_b._variable_shape)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.int64)
}, embedding_column_a._parse_example_spec)
self.assertEqual({
    'bbb': parsing_ops.VarLenFeature(dtypes.int64)
}, embedding_column_b._parse_example_spec)
