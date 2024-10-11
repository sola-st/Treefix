# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
categorical_column = fc_lib.categorical_column_with_identity(
    key='aaa', num_buckets=3)
embedding_dimension = 2
initializer = init_ops.truncated_normal_initializer(mean=0.0, stddev=.5)
embedding_column = tpu_fc._TPUEmbeddingColumnV2(
    categorical_column=categorical_column,
    dimension=embedding_dimension,
    combiner='mean',
    initializer=initializer,
    max_sequence_length=0,
    learning_rate_fn=None,
    use_safe_embedding_lookup=True,
    bypass_scope_validation=False)
self.assertIs(categorical_column, embedding_column.categorical_column)
self.assertEqual(embedding_dimension, embedding_column.dimension)
state_manager = _TestStateManager()
with tpu_function.tpu_shard_context(1):
    with variable_scope.variable_scope('tower1/scope1'):
        embedding_column.create_state(state_manager)
    with variable_scope.variable_scope('tower2/scope2'):
        # With default scope validation, the same column cannot be used in a new
        # variable scope.
        with self.assertRaisesRegex(ValueError,
                                    'the variable scope name is different'):
            embedding_column.create_state(state_manager)
