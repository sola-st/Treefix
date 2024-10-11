# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
def foo(rs):
    rp = RowPartition.from_row_splits(rs)
    static_nrows = rp.static_nrows
    self.assertIsNone(static_nrows)
foo(array_ops.constant([0, 3, 4, 5], dtype=dtypes.int32))
