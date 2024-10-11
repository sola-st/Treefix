# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/bfloat16_test.py
"""Test if custom name for the variable scope is propagated correctly."""
name = 'bfloat16'
with bfloat16.bfloat16_scope('bfloat16') as bf:
    self.assertEqual(bf.name, name)
