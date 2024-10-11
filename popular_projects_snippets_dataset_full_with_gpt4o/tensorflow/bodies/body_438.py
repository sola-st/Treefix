# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
text = "tf.concat(a, b)\ntf.split(a, b, c)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.concat(axis=a, values=b)\n"
                 "tf.split(axis=a, num_or_size_splits=b, value=c)\n")
