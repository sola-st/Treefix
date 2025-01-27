# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.summary.graph(my_graph)"
_, _, errors, _ = self._upgrade(text)
expected_error = "tf.compat.v2.summary.trace"
self.assertIn(expected_error, errors[0])
