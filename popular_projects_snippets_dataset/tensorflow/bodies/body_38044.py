# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
with self.assertRaisesRegex(
    Exception, (r"(In\[0\] and In\[1\] has different ndims|In\[0\] "
                r"ndims must be >= 2|Shape must be rank 2 but is rank 1)")):
    infix_matmul(
        ops.convert_to_tensor([10.0, 20.0, 30.0]),
        ops.convert_to_tensor([[40.0, 50.0], [60.0, 70.0]]))
