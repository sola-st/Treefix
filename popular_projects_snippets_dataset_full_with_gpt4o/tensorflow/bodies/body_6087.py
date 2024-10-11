# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
"""Restore to variables with mirroring in a fresh graph."""
with self.session(graph=ops.Graph()) as sess:
    mirrored = _make_mirrored(distribution)
    v = mirrored.values

    # Overwrite the initial values.
    self._assign_mirrored(mirrored, [7., 8.])

    # Restores the saved value of 3. to both variables.
    saver = saver_lib.Saver(var_list=[mirrored])
    saver.restore(sess, save_path)
    self.assertEqual([3., 3.], self.evaluate([v[0], v[1]]))
