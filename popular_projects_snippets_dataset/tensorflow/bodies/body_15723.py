# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
"""Test that rt.__getitem__(slice_spec) == expected."""
# Intentionally use an unknown shape for `splits`, to force the code path
# that deals with having nrows unknown at graph construction time.
splits = constant_op.constant(
    EXAMPLE_RAGGED_TENSOR_2D_SPLITS, dtype=dtypes.int64)
splits = array_ops.placeholder_with_default(splits, None)
rt = RaggedTensor.from_row_splits(EXAMPLE_RAGGED_TENSOR_2D_VALUES, splits)
self.assertAllEqual(rt, EXAMPLE_RAGGED_TENSOR_2D)
self._TestGetItem(rt, slice_spec, expected)
