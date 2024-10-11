# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
with self.cached_session() as sess:
    v, replica_local = _make_replica_local(
        variable_scope.VariableAggregation.SUM, distribution)

    # Overwrite the initial values.
    self._assign_replica_local(v, [3., 4.])

    with distribution.scope():
        # Saves the current value of v[0] + v[1], 7.
        save_path, saver = self._save_return_saver(sess, replica_local)

        # Change the values between save and restore.
        self._assign_replica_local(v, [5., 6.])

        # Restores the saved value of 7. which gets divided equally
        # between the variables.
        saver.restore(sess, save_path)
        self.assertEqual([3.5, 3.5], self.evaluate([v[0], v[1]]))
