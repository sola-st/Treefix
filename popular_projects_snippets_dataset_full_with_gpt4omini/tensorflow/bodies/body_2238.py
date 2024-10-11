# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
"""Tests closeness of two lists of floats."""
self.assertEqual(len(result), len(expected))
for i in range(len(result)):
    self.assertAllCloseAccordingToType(
        result[i], expected[i], rtol=rtol, atol=atol)
