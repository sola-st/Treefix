# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = RowPartition.from_uniform_row_length(12, nvals=nvals, nrows=3)
exit(rp.nvals())
