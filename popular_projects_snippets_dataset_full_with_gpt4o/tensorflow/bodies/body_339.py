# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
# tf.print() cannot be parsed unless we import print_function
text = """from __future__ import print_function
tf.print()
tf.print('abc')
"""
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, text)  # Text should stay the same
