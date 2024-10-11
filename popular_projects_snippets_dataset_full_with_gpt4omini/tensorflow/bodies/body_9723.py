# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
server1 = server_lib.Server.create_local_server()
server2 = server_lib.Server.create_local_server()
cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = 'worker'
job.tasks[0] = server1.target[len('grpc://'):]
job.tasks[1] = server2.target[len('grpc://'):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)

const = constant_op.constant(17)
sess = session.Session(server1.target, config=config)
output = self.evaluate(const)
self.assertEqual(17, output)
