# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
"""Restore to variables with mirroring in a fresh graph."""
with self.session(graph=ops.Graph()) as sess:
    v, replica_local = _make_replica_local(
        variable_scope.VariableAggregation.SUM, distribution)

    # Overwrite the initial values.
    self._assign_replica_local(v, [7., 8.])

    with distribution.scope():
        # Restores the saved value of 3.5 to both variables.
        saver = saver_lib.Saver(var_list=[replica_local])
        saver.restore(sess, save_path)
        self.assertEqual([1.75, 1.75], self.evaluate([v[0], v[1]]))
