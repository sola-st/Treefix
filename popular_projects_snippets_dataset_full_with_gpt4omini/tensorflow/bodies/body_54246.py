# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    a = array_ops.placeholder(dtype=dtypes.float32, shape=[])
    b = array_ops.ones([])
    c = a + b
    self.assertEqual(tensor_shape.TensorShape([]), c.shape)
