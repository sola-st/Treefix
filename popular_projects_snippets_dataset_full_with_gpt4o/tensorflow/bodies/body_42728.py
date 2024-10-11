# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = _create_tensor(np.zeros(0, dtype=np.float32))
self.assertTrue(repr(t).startswith("<"))
self.assertTrue(repr(t).endswith(">"))
self.assertIn("shape=(0,), dtype=float32, numpy=%r" % t.numpy(), repr(t))
