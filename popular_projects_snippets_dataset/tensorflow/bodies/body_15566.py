# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_const_op_test.py
"""Tests for the _find_scalar_and_max_depth helper function."""
if exception is not None:
    self.assertRaisesRegex(exception, message,
                           ragged_factory_ops._find_scalar_and_max_depth,
                           pylist)
else:
    self.assertEqual(
        ragged_factory_ops._find_scalar_and_max_depth(pylist),
        (scalar_depth, max_depth))
