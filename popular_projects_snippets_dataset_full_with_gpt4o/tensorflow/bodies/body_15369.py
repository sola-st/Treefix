# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Merge with a TypeSpec to create a new RowPartition."""
a_spec = self._type_spec
if not a_spec.is_compatible_with(b):
    # TODO(martinz): Should a dynamic check be used here?
    raise ValueError("RowPartition and RowPartitionSpec are not compatible")
nrows = constant_op.constant(
    b.nrows, self.dtype) if b.nrows is not None else self._nrows
nvals = constant_op.constant(
    b.nvals, self.dtype) if b.nvals is not None else self._nvals
uniform_row_length = constant_op.constant(
    b.uniform_row_length, self.dtype
) if b.uniform_row_length is not None else self._uniform_row_length
exit(RowPartition(
    row_splits=self._row_splits,
    row_lengths=self._row_lengths,
    value_rowids=self._value_rowids,
    nvals=nvals,
    uniform_row_length=uniform_row_length,
    nrows=nrows,
    internal=_row_partition_factory_key))
