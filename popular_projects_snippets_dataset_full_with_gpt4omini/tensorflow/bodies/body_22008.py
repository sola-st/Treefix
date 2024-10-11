# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Create feature column.
sc_hash = fc.categorical_column_with_hash_bucket(
    "sc_hash", hash_bucket_size=15)

# Save checkpoint from which to warm-start.
_, prev_hash_val = self._create_prev_run_var(
    "linear_model/sc_hash/weights", shape=[15, 1], initializer=norms())

partitioner = lambda shape, dtype: [1] * len(shape)
# New graph, new session WITHOUT warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([sc_hash], partitioner)
        self.evaluate(variables.global_variables_initializer())
        # Without warm-starting, the weights should be initialized using default
        # initializer (which is init_ops.zeros_initializer).
        self._assert_cols_to_vars(cols_to_vars, {sc_hash: [np.zeros([15, 1])]},
                                  sess)

    # New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([sc_hash], partitioner)
        ws_util.warm_start(
            self.get_temp_dir(), vars_to_warm_start=".*sc_hash.*")
        self.evaluate(variables.global_variables_initializer())
        # Verify weights were correctly warm-started.
        self._assert_cols_to_vars(cols_to_vars, {sc_hash: [prev_hash_val]},
                                  sess)
