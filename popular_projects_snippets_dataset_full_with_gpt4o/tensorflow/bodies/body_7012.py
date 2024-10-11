# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/warm_starting_util_test.py
with self.session(graph=g) as sess:
    # Initialize with zeros.
    var = variable_scope.get_variable(
        var_name, initializer=[[0., 0.], [0., 0.]])
    ws_util.warm_start(self.get_temp_dir())
    sess.run(variables.global_variables_initializer())
    # Verify weights were correctly warm-started to previous values.
    self.assertAllEqual(original_value, self.evaluate(var))
