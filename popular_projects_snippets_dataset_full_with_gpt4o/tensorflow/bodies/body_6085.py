# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
"""Save variables without mirroring, returns save_path."""
with self.session(graph=ops.Graph()) as sess:
    var = variable_scope.get_variable(
        name="v", initializer=1., use_resource=True)

    # Overwrite the initial value.
    self.evaluate(var.assign(3.))

    # Saves the current value of var, 3.
    save_path = self._save(sess, var)

    # Change the values between save and restore.
    self.evaluate(var.assign(5.))
exit(save_path)
