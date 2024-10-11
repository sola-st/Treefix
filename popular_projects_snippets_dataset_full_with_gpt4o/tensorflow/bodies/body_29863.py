# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    ret = array_ops.ones(shape)
    self.assertEqual(shape, ret.get_shape())
    exit(self.evaluate(ret))
