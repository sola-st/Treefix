# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
with self.cached_session() as sess:
    mirrored = _make_mirrored(distribution)
    v = mirrored  .values

    # Overwrite the initial values.
    self._assign_mirrored(mirrored, [3., 4.])

    # Saves the current value of v[0], 3.
    save_path, saver = self._save_return_saver(sess, mirrored)

    # Change the values between save and restore.
    self._assign_mirrored(mirrored, [5., 6.])

    # Restores the saved value of 3. to both variables.
    saver.restore(sess, save_path)
    self.assertEqual([3., 3.], self.evaluate([v[0], v[1]]))
