# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = _create_tensor(np.eye(3))
tensor_repr = repr(t)
self.assertTrue(tensor_repr.startswith("<"))
self.assertTrue(tensor_repr.endswith(">"))
self.assertIn(
    "shape=%s, dtype=%s, numpy=\n%r" % (t.shape, t.dtype.name, t.numpy()),
    tensor_repr)
