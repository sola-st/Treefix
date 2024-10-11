# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Create feature column.
real = fc.numeric_column("real")
real_bucket = fc.bucketized_column(real, boundaries=[0., 1., 2., 3.])

# Save checkpoint from which to warm-start.
_, prev_bucket_val = self._create_prev_run_var(
    "linear_model/real_bucketized/weights",
    shape=[5, 1],
    initializer=norms())

partitioner = lambda shape, dtype: [1] * len(shape)
# New graph, new session WITHOUT warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([real_bucket], partitioner)
        self.evaluate(variables.global_variables_initializer())
        # Without warm-starting, the weights should be initialized using default
        # initializer (which is init_ops.zeros_initializer).
        self._assert_cols_to_vars(cols_to_vars,
                                  {real_bucket: [np.zeros([5, 1])]}, sess)

    # New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model([real_bucket], partitioner)
        ws_util.warm_start(
            self.get_temp_dir(), vars_to_warm_start=".*real_bucketized.*")
        self.evaluate(variables.global_variables_initializer())
        # Verify weights were correctly warm-started.
        self._assert_cols_to_vars(cols_to_vars,
                                  {real_bucket: [prev_bucket_val]}, sess)
