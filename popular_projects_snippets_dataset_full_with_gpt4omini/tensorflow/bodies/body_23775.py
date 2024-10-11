# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
"""Tests that negative zero and zero hash to the same value."""
self.assertEqual(hash(float_type(-0.0)), hash(float_type(0.0)))
