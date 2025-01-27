# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
vocabulary_size = 3
categorical_column_a = fc_lib.categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
categorical_column_b = fc_lib.categorical_column_with_identity(
    key='bbb', num_buckets=vocabulary_size)
embedding_dimension = 2
embedding_column_a, embedding_column_b = tpu_fc.shared_embedding_columns_v2(
    [categorical_column_a, categorical_column_b],
    dimension=embedding_dimension,
    combiner='my_combiner',
    initializer=lambda: 'my_initializer',
    shared_embedding_collection_name='var_scope_name')
self.assertIs(categorical_column_a, embedding_column_a.categorical_column)
self.assertIs(categorical_column_b, embedding_column_b.categorical_column)
self.assertEqual((vocabulary_size, embedding_dimension),
                 embedding_column_a.get_embedding_table_size())
self.assertEqual((vocabulary_size, embedding_dimension),
                 embedding_column_a.get_embedding_table_size())
self.assertEqual('my_combiner', embedding_column_a.combiner)
self.assertEqual('my_combiner', embedding_column_b.combiner)
self.assertEqual('my_initializer', embedding_column_a.get_initializer()())
self.assertEqual('my_initializer', embedding_column_b.get_initializer()())
self.assertEqual('var_scope_name',
                 embedding_column_a.get_embedding_var_name())
self.assertEqual('var_scope_name',
                 embedding_column_b.get_embedding_var_name())
self.assertEqual('aaa_shared_embedding', embedding_column_a.name)
self.assertEqual('bbb_shared_embedding', embedding_column_b.name)
self.assertEqual((embedding_dimension,), embedding_column_a.variable_shape)
self.assertEqual((embedding_dimension,), embedding_column_b.variable_shape)
