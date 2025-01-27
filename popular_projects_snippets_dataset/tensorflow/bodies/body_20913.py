# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_same_variables_clear_test.py
server = server_lib.Server.create_local_server()

# Creates a graph with 2 variables.
v0 = variables.Variable([[2, 1]], name="v0")
v1 = variables.Variable([[1], [2]], name="v1")
v2 = math_ops.matmul(v0, v1)

# Verifies that both sessions connecting to the same target return
# the same results.
sess_1 = session.Session(server.target)
sess_2 = session.Session(server.target)
sess_1.run(variables.global_variables_initializer())
self.assertAllEqual([[4]], sess_1.run(v2))
self.assertAllEqual([[4]], sess_2.run(v2))

# Resets target. sessions abort. Use sess_2 to verify.
session.Session.reset(server.target)
with self.assertRaises(errors_impl.AbortedError):
    self.assertAllEqual([[4]], sess_2.run(v2))

# Connects to the same target. Device memory for the variables would have
# been released, so they will be uninitialized.
sess_2 = session.Session(server.target)
with self.assertRaises(errors_impl.FailedPreconditionError):
    sess_2.run(v2)
# Reinitializes the variables.
sess_2.run(variables.global_variables_initializer())
self.assertAllEqual([[4]], sess_2.run(v2))
sess_2.close()
