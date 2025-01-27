# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Create vocab for sparse column "sc_vocab".
vocab_path = self._write_vocab(["apple", "banana", "guava", "orange"],
                               "vocab")

# Create feature columns.
sc_int = fc.categorical_column_with_identity("sc_int", num_buckets=10)
sc_hash = fc.categorical_column_with_hash_bucket(
    "sc_hash", hash_bucket_size=15)
sc_keys = fc.categorical_column_with_vocabulary_list(
    "sc_keys", vocabulary_list=["a", "b", "c", "e"])
sc_vocab = fc.categorical_column_with_vocabulary_file(
    "sc_vocab", vocabulary_file=vocab_path, vocabulary_size=4)
real = fc.numeric_column("real")
real_bucket = fc.bucketized_column(real, boundaries=[0., 1., 2., 3.])
cross = fc.crossed_column([sc_keys, sc_vocab], hash_bucket_size=20)
all_linear_cols = [sc_int, sc_hash, sc_keys, sc_vocab, real_bucket, cross]

# Save checkpoint from which to warm-start.  Also create a bias variable,
# so we can check that it's also warm-started.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        sc_int_weights = variable_scope.get_variable(
            "linear_model/sc_int/weights", shape=[10, 1], initializer=ones())
        sc_hash_weights = variable_scope.get_variable(
            "linear_model/sc_hash/weights", shape=[15, 1], initializer=norms())
        sc_keys_weights = variable_scope.get_variable(
            "linear_model/sc_keys/weights", shape=[4, 1], initializer=rand())
        sc_vocab_weights = variable_scope.get_variable(
            "linear_model/sc_vocab/weights", shape=[4, 1], initializer=ones())
        real_bucket_weights = variable_scope.get_variable(
            "linear_model/real_bucketized/weights",
            shape=[5, 1],
            initializer=norms())
        cross_weights = variable_scope.get_variable(
            "linear_model/sc_keys_X_sc_vocab/weights",
            shape=[20, 1],
            initializer=rand())
        bias = variable_scope.get_variable(
            "linear_model/bias_weights",
            shape=[1],
            initializer=rand())
        self._write_checkpoint(sess)
        (prev_int_val, prev_hash_val, prev_keys_val, prev_vocab_val,
         prev_bucket_val, prev_cross_val, prev_bias_val) = sess.run([
             sc_int_weights, sc_hash_weights, sc_keys_weights, sc_vocab_weights,
             real_bucket_weights, cross_weights, bias
         ])

partitioner = lambda shape, dtype: [1] * len(shape)
# New graph, new session WITHOUT warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model(all_linear_cols, partitioner)
        self.evaluate(variables.global_variables_initializer())
        # Without warm-starting, all weights should be initialized using default
        # initializer (which is init_ops.zeros_initializer).
        self._assert_cols_to_vars(cols_to_vars, {
            sc_int: [np.zeros([10, 1])],
            sc_hash: [np.zeros([15, 1])],
            sc_keys: [np.zeros([4, 1])],
            sc_vocab: [np.zeros([4, 1])],
            real_bucket: [np.zeros([5, 1])],
            cross: [np.zeros([20, 1])],
        }, sess)

    # New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model(all_linear_cols, partitioner)
        vocab_info = ws_util.VocabInfo(
            new_vocab=sc_vocab.vocabulary_file,
            new_vocab_size=sc_vocab.vocabulary_size,
            num_oov_buckets=sc_vocab.num_oov_buckets,
            old_vocab=vocab_path)
        ws_util.warm_start(
            self.get_temp_dir(),
            var_name_to_vocab_info={
                "linear_model/sc_vocab/weights": vocab_info
            })
        self.evaluate(variables.global_variables_initializer())
        # Verify weights were correctly warm-started.
        self._assert_cols_to_vars(cols_to_vars, {
            sc_int: [prev_int_val],
            sc_hash: [prev_hash_val],
            sc_keys: [prev_keys_val],
            sc_vocab: [prev_vocab_val],
            real_bucket: [prev_bucket_val],
            cross: [prev_cross_val],
            "bias": [prev_bias_val],
        }, sess)
