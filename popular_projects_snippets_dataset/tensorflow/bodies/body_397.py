# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
"""Tests for transforming from tf.strings.split."""
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
