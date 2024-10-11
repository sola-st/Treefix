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
job1.name = 'worker1'
job1.tasks[0] = server2.target[len('grpc://'):]
job1.tasks[1] = server1.target[len('grpc://'):]

cluster_def2 = cluster_pb2.ClusterDef()
job2 = cluster_def2.job.add()
job2.name = 'worker2'
job2.tasks[0] = server2.target[len('grpc://'):]
job2.tasks[1] = server3.target[len('grpc://'):]

config1 = config_pb2.ConfigProto(cluster_def=cluster_def1)
config2 = config_pb2.ConfigProto(cluster_def=cluster_def2)

with ops.Graph().as_default() as g1:
    with ops.device('/job:worker1/task:1'):
        var1 = variables.Variable(array_ops.zeros([2]), name='var1')
        update_op1 = state_ops.assign_add(
            var1, array_ops.ones([2]), name='var1_assign_add')
        init1 = variables.global_variables_initializer()

with ops.Graph().as_default() as g2:
    with ops.device('/job:worker2/task:1'):
        var2 = variables.Variable(array_ops.zeros([2]), name='var2')
        update_op2 = state_ops.assign_add(
            var2, array_ops.ones([2]), name='var2_assign_add')
        init2 = variables.global_variables_initializer()

sess1 = session.Session(server2.target, graph=g1, config=config1)
sess2 = session.Session(server2.target, graph=g2, config=config2)

init1.run(session=sess1)
init2.run(session=sess2)

expected_zeros = np.zeros([2])
expected_ones = np.ones([2])

self.assertAllEqual(expected_zeros, sess1.run(var1))
self.assertAllEqual(expected_zeros, sess2.run(var2))

self.assertAllEqual(expected_ones, sess1.run(update_op1))
self.assertAllEqual(expected_ones, sess1.run(var1))
self.assertAllEqual(expected_zeros, sess2.run(var2))
self.assertAllEqual(expected_ones, sess2.run(update_op2))
self.assertAllEqual(expected_ones + expected_ones, sess1.run(update_op1))
self.assertAllEqual(expected_ones, sess2.run(var2))
self.assertAllEqual(expected_ones + expected_ones, sess1.run(var1))
