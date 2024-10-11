# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.summary.always_record_summaries()"
expected = "tf.compat.v2.summary.record_if(True)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
