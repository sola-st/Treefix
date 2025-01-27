# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_safety_test.py
text = "from tensorflow.google.compat import v1 as tf"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(text, new_text)

text = "from tensorflow.google.compat import v2 as tf"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(text, new_text)
