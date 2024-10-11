# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t_np_orig = np.array([[b"a", b"ab"], [b"abc", b"abcd"]])
t = _create_tensor(t_np_orig)
t_np = t.numpy()
self.assertTrue(np.all(t_np == t_np_orig), "%s vs %s" % (t_np, t_np_orig))
