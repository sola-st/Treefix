# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
cdim = constant_op.constant(1, dtypes.int32)
s0 = constant_op.constant([2, 3, 5], dtypes.int32)
s1 = constant_op.constant([2, 7, 10], dtypes.int32)
off = gen_array_ops.concat_offset(cdim, [s0, s1])
with self.assertRaisesRegex(
    errors_impl.InvalidArgumentError,
    r"All dimensions except 1 must match. Input 1 has shape \[2 7 10\] "
    r"and doesn't match input 0 with shape \[2 3 5\]."):
    self.evaluate(off)
