# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
with ops.Graph().as_default():
    # Creates variable with container name.
    with ops.container("test0"):
        v0 = variables.VariableV1(1.0, name="v0")
    # Creates variable with default container.
    v1 = variables.VariableV1(2.0, name="v1")
    # Verifies resetting the non-existent target returns error.
    with self.assertRaises(errors_impl.NotFoundError):
        session.Session.reset("nonexistent", ["test0"])

    # Verifies resetting with config.
    # Verifies that resetting target with no server times out.
    with self.assertRaises(errors_impl.DeadlineExceededError):
        session.Session.reset(
            "grpc://localhost:0", ["test0"],
            config=config_pb2.ConfigProto(operation_timeout_in_ms=5))

    # Verifies no containers are reset with non-existent container.
    server = self._cached_server
    sess = session.Session(server.target)
    sess.run(variables.global_variables_initializer())
    self.assertAllEqual(1.0, sess.run(v0))
    self.assertAllEqual(2.0, sess.run(v1))
    # No container is reset, but the server is reset.
    session.Session.reset(server.target, ["test1"])
    # Verifies that both variables are still valid.
    sess = session.Session(server.target)
    self.assertAllEqual(1.0, sess.run(v0))
    self.assertAllEqual(2.0, sess.run(v1))
