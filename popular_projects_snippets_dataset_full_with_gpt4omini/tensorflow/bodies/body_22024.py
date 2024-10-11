# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
prev_val = [[0.5], [1.], [1.5], [2.]]
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        prev_var = variable_scope.get_variable(
            "fruit_weights",
            initializer=prev_val)
        self.evaluate(variables.global_variables_initializer())
        # Save object-based checkpoint.
        tracking_util.Checkpoint(v=prev_var).save(
            os.path.join(self.get_temp_dir(), "checkpoint"))

with ops.Graph().as_default() as g:
    with self.session(graph=g):
        fruit_weights = variable_scope.get_variable(
            "fruit_weights", initializer=[[0.], [0.], [0.], [0.]])
        ws_util.warm_start(self.get_temp_dir())
        self.evaluate(variables.global_variables_initializer())
        self.assertAllClose(prev_val, self.evaluate(fruit_weights))
