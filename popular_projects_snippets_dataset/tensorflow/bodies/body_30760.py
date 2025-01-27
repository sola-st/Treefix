# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
cdim = constant_op.constant(4, dtypes.int32)
s0 = constant_op.constant([2, 3, 5], dtypes.int32)
s1 = constant_op.constant([2, 7, 5], dtypes.int32)
off = gen_array_ops.concat_offset(cdim, [s0, s1])
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            r"Concat dim is out of range: 4 vs. 3"):
    self.evaluate(off)
