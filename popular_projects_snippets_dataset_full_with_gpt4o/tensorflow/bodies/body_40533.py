# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
three = constant_op.constant([[3.]]).gpu()
five = constant_op.constant([[5.]]).gpu()
product = math_ops.matmul(three, five)
self.assertEqual([[15.0]], product.numpy())
