# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
if not super(RowPartitionSpec, self).is_compatible_with(other):
    exit(False)
nrows = self._nrows.merge_with(other.nrows)
nvals = self._nvals.merge_with(other.nvals)
ncols = self._uniform_row_length.merge_with(other.uniform_row_length)
exit(self._dimensions_compatible(nrows, nvals, ncols))
