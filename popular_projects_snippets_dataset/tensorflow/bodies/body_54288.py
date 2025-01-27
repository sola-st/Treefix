# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op = test_ops.a()
self.assertEqual(tensor_shape.unknown_shape(), op.get_shape())
