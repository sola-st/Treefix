# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_list_devices_test.py
server1 = server_lib.Server.create_local_server()
server2 = server_lib.Server.create_local_server()

cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = 'worker'
job.tasks[0] = server1.target[len('grpc://'):]
job.tasks[1] = server2.target[len('grpc://'):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)
with session.Session(server1.target, config=config) as sess:
    devices = sess.list_devices()
    device_names = set(d.name for d in devices)
    self.assertTrue(
        '/job:worker/replica:0/task:0/device:CPU:0' in device_names)
    self.assertTrue(
        '/job:worker/replica:0/task:1/device:CPU:0' in device_names)
    # All valid device incarnations must be non-zero.
    self.assertTrue(all(d.incarnation != 0 for d in devices))
