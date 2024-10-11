# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
"""Boots 3 servers, ensures appropriate communication across workers.

    Additionally, in this cluster, we ensure the master is not the 0-th worker.

    Note: this test only uses one session.
    """
server1 = server_lib.Server.create_local_server()
server2 = server_lib.Server.create_local_server()
server3 = server_lib.Server.create_local_server()
cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = 'worker'
job.tasks[0] = server3.target[len('grpc://'):]
job.tasks[1] = server2.target[len('grpc://'):]
job.tasks[2] = server1.target[len('grpc://'):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)

# Add ops to the devices in non-linear order.

with ops.device('/job:worker/task:1'):
    feed1 = array_ops.placeholder(dtypes.float32, shape=(2))
    const1 = constant_op.constant(2.0)
    mul1 = const1 * feed1

with ops.device('/job:worker/task:2'):
    feed2 = array_ops.placeholder(dtypes.float32, shape=(2))
    const2 = constant_op.constant(2.0)
    mul2 = const2 * feed2

with ops.device('/job:worker/task:0'):
    feed0 = array_ops.placeholder(dtypes.float32, shape=(2))
    const0 = constant_op.constant(2.0)
    mul0 = const0 * feed0

sum_op = mul0 + mul1 + mul2

ones = np.ones([2])
run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata = config_pb2.RunMetadata()

# Run!
with session.Session(server1.target, config=config) as sess:
    output = sess.run(
        sum_op,
        options=run_options,
        run_metadata=run_metadata,
        feed_dict={feed1: ones,
                   feed2: ones,
                   feed0: ones})
    self.assertAllEqual(6 * ones, output)

    self.assertEqual(
        3,
        len([
            dev_stats.device
            for dev_stats in run_metadata.step_stats.dev_stats
            for node_stats in dev_stats.node_stats
            if '/job:worker/replica:0/task:' in dev_stats.device and
            node_stats.node_name.startswith('Const')
        ]), run_metadata)
