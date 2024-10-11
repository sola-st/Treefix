# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_const_op_test.py
"""Tests that `ragged_const()` raises an expected exception."""
self.assertRaisesRegex(
    exception,
    message,
    ragged_factory_ops.constant,
    pylist,
    dtype=dtype,
    ragged_rank=ragged_rank,
    inner_shape=inner_shape)
