# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_constant_value_op_test.py
"""Tests that `constant_value()` raises an expected exception."""
self.assertRaisesRegex(
    exception,
    message,
    ragged_factory_ops.constant_value,
    pylist,
    dtype=dtype,
    ragged_rank=ragged_rank,
    inner_shape=inner_shape)
