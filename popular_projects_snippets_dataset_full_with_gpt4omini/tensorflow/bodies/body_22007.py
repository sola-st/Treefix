# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Create feature column.
sc_int = fc.categorical_column_with_identity("sc_int", num_buckets=10)

# Save checkpoint from which to warm-start.
_, prev_int_val = self._create_prev_run_var(
    "linear_model/sc_int/weights", shape=[10, 1], initializer=ones())
# Verify we initialized the values correctly.
self.assertAllEqual(np.ones([10, 1]), prev_int_val)

partitioner = lambda shape, dtype: [1] * len(shape)
# New graph, new session WITHOUT warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([sc_int], partitioner)
        self.evaluate(variables.global_variables_initializer())
        # Without warm-starting, the weights should be initialized using default
        # initializer (which is init_ops.zeros_initializer).
        self._assert_cols_to_vars(cols_to_vars, {sc_int: [np.zeros([10, 1])]},
                                  sess)

    # New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([sc_int], partitioner)
        ws_util.warm_start(self.get_temp_dir(), vars_to_warm_start=".*sc_int.*")
        self.evaluate(variables.global_variables_initializer())
        # Verify weights were correctly warm-started.
        self._assert_cols_to_vars(cols_to_vars, {sc_int: [prev_int_val]}, sess)
