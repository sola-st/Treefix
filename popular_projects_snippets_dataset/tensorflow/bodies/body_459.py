# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_safety_test.py
text = "from tensorflow import foo"
expected_text = "from tensorflow.compat.v1 import foo"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "from tensorflow.foo import bar"
expected_text = "from tensorflow.compat.v1.foo import bar"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "from tensorflow import *"
expected_text = "from tensorflow.compat.v1 import *"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
