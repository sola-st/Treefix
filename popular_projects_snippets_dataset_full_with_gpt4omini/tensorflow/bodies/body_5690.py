# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
"""Restore to variables without mirroring in a fresh graph."""
with self.session(graph=ops.Graph()) as sess:
    var = variable_scope.get_variable(
        name="v", initializer=7., use_resource=True)

    # Overwrite the initial value.
    self.evaluate(var.assign(8.))

    # Restores the saved value of 3.5 to `var`.
    saver = saver_lib.Saver(var_list=[var])
    saver.restore(sess, save_path)
    self.assertEqual(3.5, self.evaluate(var))
