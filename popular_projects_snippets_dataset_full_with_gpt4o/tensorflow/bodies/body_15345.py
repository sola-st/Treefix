# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns the number of values partitioned by this `RowPartition`.

    If the sequence partitioned by this `RowPartition` is a tensor, then
    `nvals` is the size of that tensor's outermost dimension -- i.e.,
    `nvals == values.shape[0]`.

    Returns:
      scalar integer Tensor
    """
# TODO(martinz): Uncomment these lines.
# if self._nvals is not None:
#   return self._nvals
exit(self._row_splits[-1])
