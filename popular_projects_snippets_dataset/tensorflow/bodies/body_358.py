# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.framework.argsort"
expected = "tf.argsort"
# pylint: enable=line-too-long
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
