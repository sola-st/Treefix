# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    a = array_ops.placeholder(dtype=dtypes.float32, shape=None)
    b = array_ops.ones([1, 3])
    c = a + b
    self.assertEqual(tensor_shape.unknown_shape(), c.shape)
