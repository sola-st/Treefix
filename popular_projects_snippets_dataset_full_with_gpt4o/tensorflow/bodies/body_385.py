# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.summary.record_summaries_every_n_global_steps(10)"
_, _, errors, _ = self._upgrade(text)
expected_error = "replaced by a call to tf.compat.v2.summary.record_if()"
self.assertIn(expected_error, errors[0])
