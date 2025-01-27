# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
"""Test that rt.__getitem__(slice_spec) == expected."""
rt = RaggedTensor.from_row_splits([], [0])
self._TestGetItemException(rt, slice_spec, expected, message)
