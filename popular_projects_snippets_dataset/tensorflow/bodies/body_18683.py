# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
c = constant_op.constant([1.0, 2.0, 3.0])
with self.assertRaisesRegex(TypeError,
                            r"Invalid type for initial value: .*Tensor.*"):
    init_ops_v2.constant_initializer(c)
v = variables.Variable([3.0, 2.0, 1.0])
with self.assertRaisesRegex(
    TypeError, r"Invalid type for initial value: .*Variable.*"):
    init_ops_v2.constant_initializer(v)
