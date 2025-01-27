# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Create vocab for sparse column "sc_vocab".
vocab_path = self._write_vocab(["apple", "banana", "guava", "orange"],
                               "vocab")
# Create feature column.
sc_vocab = fc.categorical_column_with_vocabulary_file(
    "sc_vocab", vocabulary_file=vocab_path, vocabulary_size=4)

# Save checkpoint from which to warm-start.
_, prev_vocab_val = self._create_prev_run_var(
    "linear_model/sc_vocab/weights", shape=[4, 1], initializer=ones())

partitioner = lambda shape, dtype: [1] * len(shape)
# New graph, new session WITHOUT warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([sc_vocab], partitioner)
        self.evaluate(variables.global_variables_initializer())
        # Without warm-starting, the weights should be initialized using default
        # initializer (which is init_ops.zeros_initializer).
        self._assert_cols_to_vars(cols_to_vars, {sc_vocab: [np.zeros([4, 1])]},
                                  sess)

    # New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([sc_vocab], partitioner)
        # Since old vocab is not explicitly set in WarmStartSettings, the old
        # vocab is assumed to be same as new vocab.
        ws_util.warm_start(
            self.get_temp_dir(), vars_to_warm_start=".*sc_vocab.*")
        self.evaluate(variables.global_variables_initializer())
        # Verify weights were correctly warm-started.
        self._assert_cols_to_vars(cols_to_vars, {sc_vocab: [prev_vocab_val]},
                                  sess)
