# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
empty = constant_op.constant([], dtype=dtypes.int32)
result = array_ops.unstack(empty, 0)
self.assertIsInstance(result, list)
self.assertEmpty(result)
