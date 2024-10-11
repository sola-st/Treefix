# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
ret = array_ops.zeros(shape)
self.assertEqual(shape, ret.get_shape())
exit(ret.numpy())
