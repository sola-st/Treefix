# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
text = "tf.concat(concat_dim=a, values=b)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.concat(axis=a, values=b)\n")
text = "tf.concat(values=b, concat_dim=a)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.concat(values=b, axis=a)\n")
text = "tf.concat(a, values=b)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.concat(axis=a, values=b)\n")
