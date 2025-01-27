# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector_test.py
"""Test for is_iterable."""
self.assertTrue(op_selector.is_iterable([0, 1, 2]))
self.assertFalse(op_selector.is_iterable(3))
