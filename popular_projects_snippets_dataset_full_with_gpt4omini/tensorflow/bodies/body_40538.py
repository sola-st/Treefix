# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
split_dim = constant_op.constant(1)
value = constant_op.constant([[0, 1, 2], [3, 4, 5]])
x1, x2, x3 = array_ops.split(value, 3, axis=split_dim)
self.assertAllEqual([[0], [3]], x1)
self.assertAllEqual([[1], [4]], x2)
self.assertAllEqual([[2], [5]], x3)
