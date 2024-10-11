# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
"""Verify that nans don't propagate where they shouldn't."""
self._testNan(array_ops.where)
self._testNan(array_ops.where_v2)
