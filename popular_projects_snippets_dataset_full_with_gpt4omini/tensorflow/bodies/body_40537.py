# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
three = constant_op.constant([[3]])
five = constant_op.constant([[5]])
product = math_ops.matmul(three, five, transpose_a=True)
self.assertAllEqual([[15]], product)
