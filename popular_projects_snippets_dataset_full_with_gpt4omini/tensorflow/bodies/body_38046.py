# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
a = ops.convert_to_tensor([[10.0, 20.0, 30.0]])
b = ops.convert_to_tensor([[40.0, 50.0], [60.0, 70.0], [80.0, 90.0]])
c = infix_matmul(a, b)
self.assertEqual(c.op.type, "MatMul")
