# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = constant_op.constant(1, dtype=dtypes.int32)
three_x = x + x + x
self.assertEqual(dtypes.int32, three_x.dtype)
self.assertAllEqual(3, three_x)
