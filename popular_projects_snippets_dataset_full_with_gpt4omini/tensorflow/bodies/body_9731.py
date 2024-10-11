# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
"""Boots 3 servers, creates 2 sessions, ensures appropriate operations.

    We create 2 clusterspecs:
     1. server2 as the master, server1 as a worker
     2. server2 as the master, server3 as a worker

    We ensure that variables on the workers are independent.
    """
server1 = server_lib.Server.create_local_server()
server2 = server_lib.Server.create_local_server()
server3 = server_lib.Server.create_local_server()
cluster_def1 = cluster_pb2.ClusterDef()
job1 = cluster_def1.job.add()
job1.name = 'worker'
job1.tasks[0] = server2.target[len('grpc://'):]
job1.tasks[1] = server1.target[len('grpc://'):]

cluster_def2 = cluster_pb2.ClusterDef()
job2 = cluster_def2.job.add()
job2.name = 'worker'
job2.tasks[0] = server2.target[len('grpc://'):]
job2.tasks[1] = server3.target[len('grpc://'):]

config1 = config_pb2.ConfigProto(cluster_def=cluster_def1)
config2 = config_pb2.ConfigProto(cluster_def=cluster_def2)

with ops.device('/job:worker/task:1'):
    var = variables.Variable(array_ops.zeros([2]), name='var')
    feed = array_ops.placeholder(dtypes.float32, shape=(2))
    update_op = var.assign_add(feed)

sess1 = session.Session(server2.target, config=config1)
sess2 = session.Session(server2.target, config=config2)

variables.global_variables_initializer().run(session=sess1)
variables.global_variables_initializer().run(session=sess2)

expected_zeros = np.zeros([2])
expected_ones = np.ones([2])

self.assertAllEqual(expected_zeros, sess1.run(var))
self.assertAllEqual(expected_zeros, sess2.run(var))
self.assertAllEqual(expected_ones,
                    sess1.run(update_op, feed_dict={feed: expected_ones}))
self.assertAllEqual(expected_ones, sess1.run(var))
self.assertAllEqual(expected_zeros, sess2.run(var))
self.assertAllEqual(expected_ones,
                    sess2.run(update_op, feed_dict={feed: expected_ones}))
self.assertAllEqual(expected_ones + expected_ones,
                    sess1.run(update_op, feed_dict={feed: expected_ones}))
self.assertAllEqual(expected_ones, sess2.run(var))
self.assertAllEqual(expected_ones + expected_ones, sess1.run(var))
