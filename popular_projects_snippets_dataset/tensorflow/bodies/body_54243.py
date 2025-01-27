# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    a = array_ops.zeros([2, 3])
    b = array_ops.ones([1, 3])
    c = a + b
    self.assertEqual([2, 3], c.shape)
