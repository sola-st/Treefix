# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
c = constant_op.constant([1.0, 2.0, 3.0])
with self.assertRaisesRegex(TypeError,
                            r"Invalid type for initial value=.*Tensor.*"):
    init_ops.constant_initializer(c, dtype=dtypes.float32)
v = variables.Variable([3.0, 2.0, 1.0])
with self.assertRaisesRegex(
    TypeError, r"Invalid type for initial value=.*Variable.*"):
    init_ops.constant_initializer(v, dtype=dtypes.float32)
