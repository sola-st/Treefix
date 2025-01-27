# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
_, report, _, _ = self._upgrade("tf.contrib.rnn")
self.assertIn("tf.contrib.rnn.* has been deprecated", report)
