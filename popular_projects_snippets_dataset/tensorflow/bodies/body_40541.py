# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
split_dim = constant_op.constant(1)
value = constant_op.constant([[0, 1, 2], [3, 4, 5]])
result = array_ops.split(value, 1, axis=split_dim)
self.assertIsInstance(result, list)
self.assertLen(result, 1)
self.assertAllEqual([[0, 1, 2], [3, 4, 5]], result[0])
