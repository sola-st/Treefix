# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.summary.scalar('foo', 42)"
_, report, _, _ = self._upgrade(text)
expected_info = "TF 1.x summary API cannot be automatically migrated"
self.assertIn(expected_info, report)
