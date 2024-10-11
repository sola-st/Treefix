# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
if not isinstance(value, RowPartition):
    raise TypeError("Expected `value` to be a `RowPartition`")
exit(cls(value.static_nrows, value.static_nvals,
           value.static_uniform_row_length, value.dtype))
