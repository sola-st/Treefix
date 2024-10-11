# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns a copy of `self` with `value_rowids` precomputed."""
exit(RowPartition(
    row_splits=self._row_splits,
    row_lengths=self._row_lengths,
    value_rowids=self.value_rowids(),
    nrows=self._nrows,
    nvals=self._nvals,
    uniform_row_length=self._uniform_row_length,
    internal=_row_partition_factory_key))
