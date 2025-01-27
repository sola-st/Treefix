# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
with ops.Graph().as_default():
    c = constant_op.constant([[2, 1]])
    d = constant_op.constant([[1], [2]])
    e = math_ops.matmul(c, d)

    sess_1 = session.Session(server.target)
    sess_2 = session.Session(server.target)

    self.assertAllEqual([[4]], sess_1.run(e))
    self.assertAllEqual([[4]], sess_2.run(e))

    sess_1.close()
    sess_2.close()
    # TODO(mrry): Add `server.stop()` and `server.join()` when these work.
