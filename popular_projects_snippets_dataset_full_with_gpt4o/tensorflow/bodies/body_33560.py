# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
op_a = linalg.LinearOperatorDiag([1., 1.])
op_sum = add_operators([op_a])
self.assertEqual(1, len(op_sum))
self.assertIs(op_sum[0], op_a)
