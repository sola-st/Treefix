# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/bfloat16_test.py
"""Test if name for the variable scope is propagated correctly."""
with bfloat16.bfloat16_scope() as bf:
    self.assertEqual(bf.name, "")
