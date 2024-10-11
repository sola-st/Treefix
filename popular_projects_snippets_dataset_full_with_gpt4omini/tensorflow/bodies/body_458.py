# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_safety_test.py
text = """
try:
  import tensorflow as tf  # import line

  tf.ones([4, 5])
except AttributeError:
  pass
"""

expected_text = """
try:
  import tensorflow.compat.v1 as tf  # import line

  tf.ones([4, 5])
except AttributeError:
  pass
"""
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
