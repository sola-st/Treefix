# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
"""Test that rt.__getitem__(slice_spec) == expected."""
# Ragged tensor
rt = RaggedTensor.from_row_splits(EXAMPLE_RAGGED_TENSOR_2D_VALUES,
                                  EXAMPLE_RAGGED_TENSOR_2D_SPLITS)

self.assertAllEqual(rt, EXAMPLE_RAGGED_TENSOR_2D)
self._TestGetItemException(rt, slice_spec, expected, message)
