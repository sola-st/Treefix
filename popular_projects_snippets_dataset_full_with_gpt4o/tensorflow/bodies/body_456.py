# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_safety_test.py
text = "import tensorflow as tf"
expected_text = ("import tensorflow.compat.v1 as tf")
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "import tensorflow as tf, other_import as y"
expected_text = ("import tensorflow.compat.v1 as tf, other_import as y")
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "import tensorflow"
expected_text = ("import tensorflow.compat.v1 as tensorflow")
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "import tensorflow.foo"
expected_text = "import tensorflow.compat.v1.foo"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "import tensorflow.foo as bar"
expected_text = "import tensorflow.compat.v1.foo as bar"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
