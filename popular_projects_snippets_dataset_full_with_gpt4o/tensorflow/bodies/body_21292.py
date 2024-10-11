# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
with session.Session(server.target, config=self._useRPCConfig()) as sess:
    c = array_ops.fill([10000, 3000], 0.5)
    expected_val = np.empty([10000, 3000], dtype=np.float32)
    expected_val.fill(0.5)
    self.assertAllEqual(expected_val, sess.run(c))
