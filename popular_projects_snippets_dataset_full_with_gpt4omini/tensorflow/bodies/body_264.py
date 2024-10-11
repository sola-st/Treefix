# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.conj(a)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.math.conj(a)\n")
text = "tf.rsqrt(tf.log_sigmoid(3.8))\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.math.rsqrt(tf.math.log_sigmoid(3.8))\n")
