# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Save checkpoint from which to warm-start.
[prev_v1_val, prev_v1_momentum_val,
 prev_v2_val, _] = self._create_prev_run_vars(
     var_names=["v1", "v1/Momentum", "v2", "v2/Momentum"],
     shapes=[[10, 1]] * 4,
     initializers=[ones()] * 4)

# New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        # Initialize with zeros.
        v1 = variable_scope.get_variable(
            "v1",
            shape=[10, 1],
            initializer=zeros())
        v1_momentum = variable_scope.get_variable(
            "v1/Momentum",
            shape=[10, 1],
            initializer=zeros())
        v2 = variable_scope.get_variable(
            "v2",
            shape=[10, 1],
            initializer=zeros())
        v2_momentum = variable_scope.get_variable(
            "v2/Momentum",
            shape=[10, 1],
            initializer=zeros())
        ws_util.warm_start(self.get_temp_dir(),
                           # This warm-starts both v1 and v1/Momentum, but only
                           # v2 (and not v2/Momentum).
                           vars_to_warm_start=["v1", "v2[^/]"])
        self.evaluate(variables.global_variables_initializer())
        # Verify the selection of weights were correctly warm-started (init
        # overridden to ones).
        self.assertAllEqual(v1, prev_v1_val)
        self.assertAllEqual(v1_momentum, prev_v1_momentum_val)
        self.assertAllEqual(v2, prev_v2_val)
        self.assertAllEqual(v2_momentum, np.zeros([10, 1]))
