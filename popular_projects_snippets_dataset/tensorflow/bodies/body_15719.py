# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
"""Test that rt.__getitem__(slice_spec) == expected."""
rt = RaggedTensor.from_nested_row_splits(
    EXAMPLE_RAGGED_TENSOR_4D_VALUES,
    [EXAMPLE_RAGGED_TENSOR_4D_SPLITS1, EXAMPLE_RAGGED_TENSOR_4D_SPLITS2])
self.assertAllEqual(rt, EXAMPLE_RAGGED_TENSOR_4D)
self._TestGetItem(rt, slice_spec, expected)
