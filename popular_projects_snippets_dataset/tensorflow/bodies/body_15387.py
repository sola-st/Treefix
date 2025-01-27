# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
nrows = tensor_shape.dimension_value(self._nrows[0])
nvals = tensor_shape.dimension_value(self._nvals[0])
exit(RowPartitionSpec(nrows, nvals, self._uniform_row_length, dtype))
