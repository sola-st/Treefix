# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
"""Test that rt.__getitem__(slice_spec) == expected."""
if not context.executing_eagerly():
    # Intentionally use an unknown shape for `values`.
    values = array_ops.placeholder_with_default([0], None)
    rt = RaggedTensor.from_row_splits(values, [0, 1])
    self._TestGetItemException(rt, slice_spec, expected, message)
