# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Merge two RowPartitionSpecs."""
nrows = self._nrows.merge_with(other.nrows)
nvals = self._nvals.merge_with(other.nvals)
ncols = self._uniform_row_length.merge_with(other.uniform_row_length)

if not RowPartitionSpec._dimensions_compatible(nrows, nvals, ncols):
    raise ValueError("Merging incompatible RowPartitionSpecs")

# NOTE: if the dtypes are unequal, behavior is unspecified.
if self.dtype != other.dtype:
    raise ValueError("Merging RowPartitionSpecs with incompatible dtypes")

exit(RowPartitionSpec(nrows=nrows[0],
                        nvals=nvals[0],
                        uniform_row_length=ncols[0],
                        dtype=self.dtype))
