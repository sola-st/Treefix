# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
categorical_column = fc._categorical_column_with_identity(
    key='aaa', num_buckets=3)
embedding_dimension = 2
original = fc._embedding_column(
    categorical_column,
    dimension=embedding_dimension,
    combiner='my_combiner',
    initializer=lambda: 'my_initializer',
    ckpt_to_load_from='my_ckpt',
    tensor_name_in_ckpt='my_ckpt_tensor',
    max_norm=42.,
    trainable=False)
for embedding_column in (original, copy.deepcopy(original)):
    self.assertEqual('aaa', embedding_column.categorical_column.name)
    self.assertEqual(3, embedding_column.categorical_column._num_buckets)
    self.assertEqual({
        'aaa': parsing_ops.VarLenFeature(dtypes.int64)
    }, embedding_column.categorical_column._parse_example_spec)

    self.assertEqual(embedding_dimension, embedding_column.dimension)
    self.assertEqual('my_combiner', embedding_column.combiner)
    self.assertEqual('my_ckpt', embedding_column.ckpt_to_load_from)
    self.assertEqual('my_ckpt_tensor', embedding_column.tensor_name_in_ckpt)
    self.assertEqual(42., embedding_column.max_norm)
    self.assertFalse(embedding_column.trainable)
    self.assertEqual('aaa_embedding', embedding_column.name)
    self.assertEqual(
        (embedding_dimension,), embedding_column._variable_shape)
    self.assertEqual({
        'aaa': parsing_ops.VarLenFeature(dtypes.int64)
    }, embedding_column._parse_example_spec)
