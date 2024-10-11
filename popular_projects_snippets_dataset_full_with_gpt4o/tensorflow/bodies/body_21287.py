# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
with ops.Graph().as_default():
    with session.Session(server.target) as sess:
        c = constant_op.constant([[2, 1]])
        d = constant_op.constant([[1], [2]])
        e = math_ops.matmul(c, d)
        self.assertAllEqual([[4]], sess.run(e))
    # TODO(mrry): Add `server.stop()` and `server.join()` when these work.
