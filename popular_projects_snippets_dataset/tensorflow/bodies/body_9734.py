# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
"""Test that two sessions using ClusterSpec propagation shares state.

    For example, the updated Variable value are visible among all worker
    sessions registered in the same server.
    """
server = server_lib.Server.create_local_server()
init_value = array_ops.placeholder(dtypes.int32, shape=[])
v = variables.Variable(init_value)

cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = 'worker'
job.tasks[0] = server.target[len('grpc://'):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)
config.experimental.share_session_state_in_clusterspec_propagation = True

sess1 = session.Session(server.target, config=config)
sess2 = session.Session(server.target, config=config)

# Initially, the variable is uninitialized in both sessions.
with self.assertRaises(errors.FailedPreconditionError):
    sess1.run(v)
with self.assertRaises(errors.FailedPreconditionError):
    sess2.run(v)

# An update in sess1 should be visible in sess2.
sess1.run(v.initializer, feed_dict={init_value: 37})
self.assertEqual(37, sess1.run(v))
self.assertEqual(37, sess2.run(v))

# Closing sess2 has no effect on the state of sess1.
sess2.close()
self.assertEqual(37, sess1.run(v))

# Subsequent sessions should see the state of existing sessions.
sess3 = session.Session(server.target, config=config)
self.assertEqual(37, sess1.run(v))
self.assertEqual(37, sess3.run(v))
