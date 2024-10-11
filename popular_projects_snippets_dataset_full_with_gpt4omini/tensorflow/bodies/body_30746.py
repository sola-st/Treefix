# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
scalar = constant_op.constant(7)
dim = array_ops.placeholder(dtypes.int32)
with self.assertRaisesRegex(
    ValueError, r"Can't concatenate scalars \(use tf\.stack instead\)"):
    array_ops.concat([scalar, scalar, scalar], dim)
