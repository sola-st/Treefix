# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
nvals = array_ops.placeholder_with_default(6, None)
ph_rowlen = array_ops.placeholder_with_default(3, None)
rt2 = RowPartition.from_uniform_row_length(
    nvals=nvals, uniform_row_length=ph_rowlen)
const_nvals2 = self.evaluate(rt2.nvals())
self.assertEqual(const_nvals2, 6)
