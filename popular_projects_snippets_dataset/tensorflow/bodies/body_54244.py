# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    a = array_ops.placeholder(dtype=dtypes.float32, shape=[2, None, 3])
    b = array_ops.placeholder(dtype=dtypes.float32, shape=[2, None, 3])
    c = a + b
    self.assertEqual([2, None, 3], c.shape.as_list())
