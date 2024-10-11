# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_safety_test.py
text = "import tensorflow.google as tf"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(text, new_text)

text = "import tensorflow.google"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(text, new_text)

text = "import tensorflow.google.compat.v1 as tf"
expected_text = "import tensorflow.google.compat.v1 as tf"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "import tensorflow.google.compat.v2 as tf"
expected_text = "import tensorflow.google.compat.v2 as tf"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
