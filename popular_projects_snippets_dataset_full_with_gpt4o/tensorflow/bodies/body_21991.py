# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
_, weights = self._create_prev_run_var(
    "fruit_weights",
    shape=[4, 1],
    initializer=[[0.5], [1.], [1.5], [2.]],
    partitioner=lambda shape, dtype: [2, 1])
prev_val = np.concatenate([weights[0], weights[1]], axis=0)

with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        fruit_weights = variable_scope.get_variable(
            "fruit_weights", initializer=[[0.], [0.], [0.], [0.]])
        prev_tensor_name, var = ws_util._get_var_info(fruit_weights)
        checkpoint_utils.init_from_checkpoint(self.get_temp_dir(),
                                              {prev_tensor_name: var})
        self.evaluate(variables.global_variables_initializer())
        self.assertAllClose(prev_val, fruit_weights.eval(sess))
