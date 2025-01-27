# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_safety_test.py
text = "import tensorflow.contrib as foo"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(text, new_text)

text = "from tensorflow import contrib"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(text, new_text)
