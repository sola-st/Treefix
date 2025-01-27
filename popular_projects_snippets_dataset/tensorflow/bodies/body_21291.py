# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
with session.Session(server.target, config=self._useRPCConfig()) as sess:
    const_val = np.empty([10000, 3000], dtype=np.float32)
    const_val.fill(0.5)
    c = constant_op.constant(const_val)
    shape_t = array_ops.shape(c)
    self.assertAllEqual([10000, 3000], sess.run(shape_t))
