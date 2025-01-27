# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_integration_test.py
"""Helper function to check that each FeatureColumn parses correctly.

    Args:
      col_name: string, name to give to the feature column. Should match
        the name that the column will parse out of the features dict.
      col_fn: function used to create the feature column. For example,
        sequence_numeric_column.
      col_arg: second arg that the target feature column is expecting.
      shape: the expected dense_shape of the feature after parsing into
        a SparseTensor.
      values: the expected values at index [0, 2, 6] of the feature
        after parsing into a SparseTensor.
    """
example = _make_sequence_example()
columns = [
    fc.categorical_column_with_identity('int_ctx', num_buckets=100),
    fc.numeric_column('float_ctx'),
    col_fn(col_name, col_arg)
]
context, seq_features = parsing_ops.parse_single_sequence_example(
    example.SerializeToString(),
    context_features=fc.make_parse_example_spec_v2(columns[:2]),
    sequence_features=fc.make_parse_example_spec_v2(columns[2:]))

with self.cached_session() as sess:
    ctx_result, seq_result = sess.run([context, seq_features])
    self.assertEqual(list(seq_result[col_name].dense_shape), shape)
    self.assertEqual(
        list(seq_result[col_name].values[[0, 2, 6]]), values)
    self.assertEqual(list(ctx_result['int_ctx'].dense_shape), [1])
    self.assertEqual(ctx_result['int_ctx'].values[0], 5)
    self.assertEqual(list(ctx_result['float_ctx'].shape), [1])
    self.assertAlmostEqual(ctx_result['float_ctx'][0], 123.6, places=1)
