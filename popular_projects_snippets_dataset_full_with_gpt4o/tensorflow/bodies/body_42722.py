# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = _create_tensor(np.eye(3))
tensor_str = str(t)
self.assertIn("shape=%s, dtype=%s" % (t.shape, t.dtype.name), tensor_str)
self.assertIn(str(t), tensor_str)
