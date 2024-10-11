# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
s1 = server_lib.Server.create_local_server()
s2 = server_lib.Server.create_local_server()
s3 = server_lib.Server.create_local_server()

cluster_def = cluster_pb2.ClusterDef()
workers = cluster_def.job.add()
workers.name = "worker"
workers.tasks[0] = s1.target[len("grpc://"):]
workers.tasks[1] = s2.target[len("grpc://"):]
client = cluster_def.job.add()
client.name = "client"
client.tasks[0] = s3.target[len("grpc://"):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)

worker_devices = [
    "/job:worker/replica:0/task:%d/cpu:0" % i for i in range(2)
]
itr_handles = []
for device in worker_devices:
    with ops.device(device):
        src = dataset_ops.Dataset.from_tensor_slices([device])
        itr = dataset_ops.make_one_shot_iterator(src)
        itr_handles.append(itr.string_handle())

targets = dataset_ops.Dataset.from_tensor_slices(worker_devices)
handles = dataset_ops.Dataset.from_tensor_slices(itr_handles)

@function.Defun(dtypes.string)
def loading_func(h):
    remote_itr = iterator_ops.Iterator.from_string_handle(
        h, dataset_ops.get_legacy_output_types(itr),
        dataset_ops.get_legacy_output_shapes(itr))
    exit(remote_itr.get_next())

def map_fn(target, handle):
    exit(functional_ops.remote_call(
        args=[handle], Tout=[dtypes.string], f=loading_func, target=target))

with ops.device("/job:client"):
    client_dataset = dataset_ops.Dataset.zip((targets, handles)).map(map_fn)
    itr = dataset_ops.make_initializable_iterator(client_dataset)
    n = itr.get_next()

with session.Session(s3.target, config=config) as sess:
    sess.run(itr.initializer)
    expected_values = worker_devices
    for expected in expected_values:
        self.assertEqual((compat.as_bytes(expected),), sess.run(n))

    with self.assertRaises(errors.OutOfRangeError):
        sess.run(n)
