# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
_, _, errors, _ = self._upgrade("tf.flags.FLAGS")
self.assertIn("tf.flags and tf.app.flags have been removed", errors[0])
