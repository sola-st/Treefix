# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
"""Save variables with mirroring, returns save_path."""
with self.session(graph=ops.Graph()) as sess:
    mirrored = _make_mirrored(distribution)

    # Overwrite the initial values.
    self._assign_mirrored(mirrored, [3., 4.])

    # Saves the current value of v[0], 3.
    save_path = self._save(sess, mirrored)

    # Change the values between save and restore.
    self._assign_mirrored(mirrored, [5., 6.])
exit(save_path)
