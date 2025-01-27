# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# A key question is whether if nrows and uniform_row_length are known,
# and nvals is given but not known statically, should we determine nvals?
# TODO(martinz): Uncomment after nvals is fixed.
# @def_function.function(
#     input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
# def foo(nvals):
#   rp = RowPartition.from_uniform_row_length(12, nvals=nvals, nrows=3,
#                                             validate=False)
#   nval_output = tensor_util.constant_value(rp.nvals())
#   self.assertEqual(nval_output, 36)
# foo(constant_op.constant(36, dtype=dtypes.int32))
pass
