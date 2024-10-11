# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
text = "tf.reduce_any(a, reduction_indices=[1, 2])\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.reduce_any(a, axis=[1, 2])\n")
