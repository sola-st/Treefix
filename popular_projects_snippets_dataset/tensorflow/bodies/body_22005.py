# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Save checkpoint from which to warm-start.
_, prev_int_val = self._create_prev_run_var("v1", shape=[10, 1],
                                            initializer=ones())
# Verify we initialized the values correctly.
self.assertAllEqual(np.ones([10, 1]), prev_int_val)

# New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        # Initialize with zeros.
        var = variable_scope.get_variable(
            "v1",
            shape=[10, 1],
            initializer=zeros())
        var2 = variable_scope.get_variable(
            "v2",
            shape=[10, 1],
            initializer=zeros())
        ws_util.warm_start(self.get_temp_dir(),
                           vars_to_warm_start=["v1", "v2"],
                           var_name_to_prev_var_name=dict(v2="v1"))
        self.evaluate(variables.global_variables_initializer())
        # Verify weights were correctly warm-started (init overridden to ones).
        self.assertAllEqual(var, prev_int_val)
        self.assertAllEqual(var2, prev_int_val)
