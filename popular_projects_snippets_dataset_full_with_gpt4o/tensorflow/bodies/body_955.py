# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
"""Tests closeness of two lists of floats."""
self.assertEqual(len(result), len(expected))
for i in range(len(result)):
    self.assertAllClose(result[i], expected[i], rtol, atol)
