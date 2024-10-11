# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
"""Creates 2 sessions with each own graph, ensures appropriate operations.

    We ensure that variables on the workers shares state.
    """
server = server_lib.Server.create_local_server()
cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = 'worker'
job.tasks[0] = server.target[len('grpc://'):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)
config.experimental.share_session_state_in_clusterspec_propagation = True

with ops.Graph().as_default() as g1:
    var1 = variables.Variable(array_ops.zeros([2]), name='var')
    update_op1 = state_ops.assign_add(
        var1, array_ops.ones([2]), name='var1_assign_add')
    init1 = variables.global_variables_initializer()

with ops.Graph().as_default() as g2:
    var2 = variables.Variable(array_ops.zeros([2]), name='var')
    update_op2 = state_ops.assign_add(
        var2, array_ops.ones([2]), name='var2_assign_add')

sess1 = session.Session(server.target, graph=g1, config=config)
sess2 = session.Session(server.target, graph=g2, config=config)

expected_zeros = np.zeros([2])
expected_ones = np.ones([2])

init1.run(session=sess1)
self.assertAllEqual(expected_zeros, sess1.run(var1))
self.assertAllEqual(expected_zeros, sess2.run(var2))

self.assertAllEqual(expected_ones, sess1.run(update_op1))
self.assertAllEqual(expected_ones, sess1.run(var1))
self.assertAllEqual(expected_ones, sess2.run(var2))
self.assertAllEqual(expected_ones + expected_ones, sess2.run(update_op2))
self.assertAllEqual(expected_ones + expected_ones, sess2.run(var2))
self.assertAllEqual(expected_ones + expected_ones, sess1.run(var1))
