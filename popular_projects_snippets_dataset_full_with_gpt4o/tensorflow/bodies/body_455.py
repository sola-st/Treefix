# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_safety_test.py
text = "tf.contrib.foo()"
_, report, _, _ = self._upgrade(text)
expected_info = "tf.contrib will not be distributed"
self.assertIn(expected_info, report)
