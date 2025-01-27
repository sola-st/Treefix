# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
nvals = array_ops.placeholder_with_default(
    constant_op.constant(6, dtype=dtypes.int64), None)
rt1 = RowPartition.from_uniform_row_length(
    nvals=nvals, uniform_row_length=3)
const_nvals1 = self.evaluate(rt1.nvals())
self.assertEqual(const_nvals1, 6)
