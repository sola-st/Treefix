# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_same_variables_clear_container_test.py
# Starts two servers with different names so they map to different
# resource "containers".
server0 = server_lib.Server(
    {
        "local0": ["localhost:0"]
    }, protocol="grpc", start=True)
server1 = server_lib.Server(
    {
        "local1": ["localhost:0"]
    }, protocol="grpc", start=True)

# Creates a graph with 2 variables.
with ops.Graph().as_default():
    v0 = variables.Variable(1.0, name="v0")
    v1 = variables.Variable(2.0, name="v0")

    # Initializes the variables. Verifies that the values are correct.
    sess_0 = session.Session(server0.target)
    sess_1 = session.Session(server1.target)
    sess_0.run(v0.initializer)
    sess_1.run(v1.initializer)
    self.assertAllEqual(1.0, sess_0.run(v0))
    self.assertAllEqual(2.0, sess_1.run(v1))

    # Resets container "local0". Verifies that v0 is no longer initialized.
    session.Session.reset(server0.target, ["local0"])
    _ = session.Session(server0.target)
    with self.assertRaises(errors_impl.FailedPreconditionError):
        self.evaluate(v0)
    # Reinitializes v0 for the following test.
    self.evaluate(v0.initializer)

    # Verifies that v1 is still valid.
    self.assertAllEqual(2.0, sess_1.run(v1))

    # Resets container "local1". Verifies that v1 is no longer initialized.
    session.Session.reset(server1.target, ["local1"])
    _ = session.Session(server1.target)
    with self.assertRaises(errors_impl.FailedPreconditionError):
        self.evaluate(v1)
    # Verifies that v0 is still valid.
    _ = session.Session(server0.target)
    self.assertAllEqual(1.0, self.evaluate(v0))
