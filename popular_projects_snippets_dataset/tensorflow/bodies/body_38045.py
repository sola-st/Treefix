# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
with self.assertRaisesRegex(
    Exception, r"(Matrix size-incompatible: In\[0\]: .* In\[1\]|"
    r"Dimensions must be equal)"):
    infix_matmul(
        ops.convert_to_tensor([[10.0, 20.0, 30.0]]),
        ops.convert_to_tensor([[40.0, 50.0], [60.0, 70.0]]))
