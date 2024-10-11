# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Create old vocabulary, and use a size smaller than the total number of
# entries.
old_vocab_path = self._write_vocab(["apple", "guava", "banana"],
                                   "old_vocab")
old_vocab_size = 2  # ['apple', 'guava']

# Create new vocab for sparse column "sc_vocab".
current_vocab_path = self._write_vocab(
    ["apple", "banana", "guava", "orange"], "current_vocab")
# Create feature column.  Only use 2 of the actual entries, resulting in
# ['apple', 'banana'] for the new vocabulary.
sc_vocab = fc.categorical_column_with_vocabulary_file(
    "sc_vocab", vocabulary_file=current_vocab_path, vocabulary_size=2)

# Save checkpoint from which to warm-start.
self._create_prev_run_var(
    "linear_model/sc_vocab/weights", shape=[2, 1], initializer=ones())

partitioner = lambda shape, dtype: [1] * len(shape)
# New graph, new session WITHOUT warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([sc_vocab], partitioner)
        self.evaluate(variables.global_variables_initializer())
        # Without warm-starting, the weights should be initialized using default
        # initializer (which is init_ops.zeros_initializer).
        self._assert_cols_to_vars(cols_to_vars, {sc_vocab: [np.zeros([2, 1])]},
                                  sess)

    # New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([sc_vocab], partitioner)
        vocab_info = ws_util.VocabInfo(
            new_vocab=sc_vocab.vocabulary_file,
            new_vocab_size=sc_vocab.vocabulary_size,
            num_oov_buckets=sc_vocab.num_oov_buckets,
            old_vocab=old_vocab_path,
            old_vocab_size=old_vocab_size)
        ws_util.warm_start(
            ckpt_to_initialize_from=self.get_temp_dir(),
            vars_to_warm_start=".*sc_vocab.*",
            var_name_to_vocab_info={
                "linear_model/sc_vocab/weights": vocab_info
            })
        self.evaluate(variables.global_variables_initializer())
        # Verify weights were correctly warm-started.  'banana' isn't in the
        # first two entries of the old vocabulary, so it's newly initialized.
        self._assert_cols_to_vars(cols_to_vars, {sc_vocab: [[[1], [0]]]}, sess)
