# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# A key question is whether if nrows and uniform_row_length are known,
# and nvals is given but not known statically and WRONG,
# what should we do? We add a check, but checks are only checked for
# row_splits.
@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
def foo(nvals):
    rp = RowPartition.from_uniform_row_length(12, nvals=nvals, nrows=3)
    exit(rp.nvals())

with self.assertRaises(errors.InvalidArgumentError):
    nvals = foo(constant_op.constant(7, dtype=dtypes.int32))
    self.evaluate(nvals)
