# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_multiple_containers_test.py
with ops.container("test0"):
    v0 = variables.Variable(1.0, name="v0")
with ops.container("test1"):
    v1 = variables.Variable(2.0, name="v0")
server = server_lib.Server.create_local_server()
sess = session.Session(server.target)
sess.run(variables.global_variables_initializer())
self.assertAllEqual(1.0, sess.run(v0))
self.assertAllEqual(2.0, sess.run(v1))

# Resets container. Session aborts.
session.Session.reset(server.target, ["test0"])
with self.assertRaises(errors_impl.AbortedError):
    sess.run(v1)

# Connects to the same target. Device memory for the v0 would have
# been released, so it will be uninitialized. But v1 should still
# be valid.
sess = session.Session(server.target)
with self.assertRaises(errors_impl.FailedPreconditionError):
    sess.run(v0)
self.assertAllEqual(2.0, sess.run(v1))
