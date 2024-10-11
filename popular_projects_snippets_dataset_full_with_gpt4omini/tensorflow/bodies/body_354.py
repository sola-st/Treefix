# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "contrib_framework.is_tensor(x)"
expected = "tf.is_tensor(x)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
