# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
text = "tf.concat(a, tf.concat(c, d))\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text, "tf.concat(axis=a, values=tf.concat(axis=c, values=d))\n")
