# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
"""Tests that result and expeted are both close and sorted."""
self.assertAllClose(result, expected, rtol, atol)
self.assertAllEqual(np.sort(result), result)
