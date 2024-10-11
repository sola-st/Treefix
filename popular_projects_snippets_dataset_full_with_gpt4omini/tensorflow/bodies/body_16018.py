# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# This originally failed to run because nrows was dtypes.int32. I think
# we may need to consider the semantics of the type of a RowPartition
# if preferred_dtype is unspecified. Also, looking at convert_to_tensor:
# dtype specifies the type of the output.
# preferred_dtype/dtype_hint is a suggestion, and dtype_hint is the new
# name.
nrows = constant_op.constant(3, dtype=dtypes.int32)
nvals = constant_op.constant(12, dtype=dtypes.int64)
row_length = constant_op.constant(4, dtype=dtypes.int64)
rp = RowPartition.from_uniform_row_length(row_length, nvals=nvals,
                                          nrows=nrows, dtype=dtypes.int64)
self.assertEqual(rp.nrows().dtype, dtypes.int64)
