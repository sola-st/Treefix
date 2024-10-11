# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
server1 = server_lib.Server.create_local_server()
server2 = server_lib.Server.create_local_server()
cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = 'worker'
job.tasks[0] = server1.target[len('grpc://'):]
job.tasks[1] = server2.target[len('grpc://'):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)

with ops.Graph().as_default() as g, ops.device(
    '/job:worker/task:1/device:CPU:0'):
    const = constant_op.constant(17)
sess = session.Session(server1.target, config=config, graph=g)
run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata = config_pb2.RunMetadata()
output = sess.run(const, options=run_options, run_metadata=run_metadata)
self.assertEqual(17, output)
self.assertEqual(1,
                 len([
                     node_stats
                     for dev_stats in run_metadata.step_stats.dev_stats
                     for node_stats in dev_stats.node_stats
                     if '/job:worker/replica:0/task:1/device:CPU:0' ==
                     dev_stats.device and 'Const' == node_stats.node_name
                 ]))
