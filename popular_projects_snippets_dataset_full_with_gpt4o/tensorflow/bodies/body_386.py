# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.summary.all_summary_ops()"
expected = "tf.compat.v1.summary.all_v2_summary_ops()"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
