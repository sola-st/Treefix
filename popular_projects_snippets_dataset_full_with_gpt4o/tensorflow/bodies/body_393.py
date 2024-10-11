# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "flags = tf.app.flags"
expected = "flags = tf.compat.v1.app.flags"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
