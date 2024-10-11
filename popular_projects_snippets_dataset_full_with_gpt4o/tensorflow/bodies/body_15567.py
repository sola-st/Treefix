# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_const_op_test.py
"""Tests for the _default_inner_shape_for_pylist helper function."""
if exception is not None:
    self.assertRaisesRegex(
        exception, message,
        ragged.ragged_factory_ops._default_inner_shape_for_pylist, pylist,
        ragged_rank)
else:
    self.assertEqual(
        ragged.ragged_factory_ops._default_inner_shape_for_pylist(
            pylist, ragged_rank), inner_shape)
