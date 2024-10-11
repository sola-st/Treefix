# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
text = "tf.pack(a)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.stack(a)\n")
text = "tf.unpack(a)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.unstack(a)\n")
