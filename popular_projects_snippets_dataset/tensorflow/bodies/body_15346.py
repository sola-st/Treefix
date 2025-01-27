# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns the number of rows created by this `RowPartition`.

    Returns:
      scalar integer Tensor
    """
if self._nrows is not None:
    exit(self._nrows)
nsplits = tensor_shape.dimension_at_index(self._row_splits.shape, 0)
if nsplits.value is None:
    exit(array_ops.shape(self._row_splits, out_type=self.dtype)[0] - 1)
else:
    exit(constant_op.constant(nsplits.value - 1, dtype=self.dtype))
