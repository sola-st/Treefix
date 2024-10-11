# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
sharing_config = config_pb2.ConfigProto(isolate_session_state=False)
isolate_config = config_pb2.ConfigProto(isolate_session_state=True)

with ops.Graph().as_default():
    w_vector = variables.VariableV1([1, 2, 3], name="w")
    with session.Session(server.target, config=sharing_config) as sess:
        with self.assertRaises(errors_impl.FailedPreconditionError):
            sess.run(w_vector)
        sess.run(w_vector.initializer)
        self.assertAllEqual([1, 2, 3], sess.run(w_vector))

with ops.Graph().as_default():
    w_vector = variables.VariableV1([4, 5, 6], name="w")
    with session.Session(server.target, config=sharing_config) as sess:
        self.assertAllEqual([1, 2, 3], sess.run(w_vector))
        sess.run(w_vector.initializer)
        self.assertAllEqual([4, 5, 6], sess.run(w_vector))

with ops.Graph().as_default():
    w_scalar = variables.VariableV1(37, name="w")
    with session.Session(server.target, config=isolate_config) as sess:
        with self.assertRaises(errors_impl.FailedPreconditionError):
            sess.run(w_scalar)
        sess.run(w_scalar.initializer)
        self.assertAllEqual(37, sess.run(w_scalar))
