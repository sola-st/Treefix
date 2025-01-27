# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
# Note: CPU->CPU transfers have a fast-path in
# BaseRemoteRendezvous::SameWorkerRecvDone that means the test doesn't
# actually capture the motivating bug unless run on a GPU machine.
#
# Example error message (before bugfix -- line breaks added because  lint):
#
# W0718 17:14:41.521534  190121 device_mgr.cc:107] Unknown device:
#     /job:worker/replica:0/task:0/device:CPU:0 all devices:
#     /job:local/replica:0/task:0/device:GPU:0,
#     /job:local/replica:0/task:0/device:GPU:0,
#     /job:local/replica:0/task:0/cpu:1, CPU:0, GPU:0,
#     /job:local/replica:0/task:0/device:CPU:1,
#     /job:local/replica:0/task:0/device:CPU:0, CPU:1,
#     /job:local/replica:0/task:0/cpu:0
server_config = config_pb2.ConfigProto(device_count={'CPU': 2})
server1 = server_lib.Server.create_local_server(config=server_config)
server2 = server_lib.Server.create_local_server(config=server_config)
cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = 'worker'
job.tasks[0] = server1.target[len('grpc://'):]
job.tasks[1] = server2.target[len('grpc://'):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)

with ops.Graph().as_default() as g:
    with ops.device('/job:worker/task:1/cpu:1'):
        input1 = constant_op.constant(17, dtypes.float32)
    with ops.device('/job:worker/task:0/cpu:1'):
        input2 = constant_op.constant(3, dtypes.float32)
    with ops.device('/job:worker/task:1/cpu:0'):
        sum1 = input1 + input2

    if test.is_gpu_available():
        device_str = '/job:worker/task:0/device:GPU:0'
    else:
        device_str = '/job:worker/task:0/cpu:1'
    with ops.device(device_str):
        sum2 = input2 + input1

    with ops.device('/job:worker/task:0/cpu:0'):
        sum3 = sum1 + sum2
with session.Session(server1.target, config=config, graph=g):
    output = self.evaluate(sum3)
self.assertEqual(40, output)
