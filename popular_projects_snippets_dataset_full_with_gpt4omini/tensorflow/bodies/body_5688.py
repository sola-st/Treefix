# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
"""Save variables with mirroring, returns save_path."""
with self.session(graph=ops.Graph()) as sess:
    v, replica_local = _make_replica_local(
        variable_scope.VariableAggregation.SUM, distribution)

    # Overwrite the initial values.
    self._assign_replica_local(v, [1.5, 2.])

    with distribution.scope():
        # Saves the current value of v[0] + v[1], 3.5
        save_path = self._save(sess, replica_local)

        # Change the values between save and restore.
        self._assign_replica_local(v, [5., 6.])
exit(save_path)
