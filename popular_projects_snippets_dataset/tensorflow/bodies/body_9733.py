# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
"""Test that two sessions using ClusterSpec propagation are isolated."""
server = server_lib.Server.create_local_server()
init_value = array_ops.placeholder(dtypes.int32, shape=[])
v = variables.Variable(init_value)

cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = 'worker'
job.tasks[0] = server.target[len('grpc://'):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)

sess1 = session.Session(server.target, config=config)
sess2 = session.Session(server.target, config=config)

# Initially, the variable is uninitialized in both sessions.
with self.assertRaises(errors.FailedPreconditionError):
    sess1.run(v)
with self.assertRaises(errors.FailedPreconditionError):
    sess2.run(v)

# An update in sess1 should be visible in sess1 only.
sess1.run(v.initializer, feed_dict={init_value: 37})
self.assertEqual(37, sess1.run(v))
with self.assertRaises(errors.FailedPreconditionError):
    sess2.run(v)

# An update in sess2 should be visible in sess2 only.
sess2.run(v.initializer, feed_dict={init_value: 86})
self.assertEqual(37, sess1.run(v))
self.assertEqual(86, sess2.run(v))

# Closing sess2 has no effect on the state of sess1.
sess2.close()
self.assertEqual(37, sess1.run(v))

# Subsequent sessions will not see the state of existing sessions.
sess3 = session.Session(server.target, config=config)
self.assertEqual(37, sess1.run(v))
with self.assertRaises(errors.FailedPreconditionError):
    sess3.run(v)
