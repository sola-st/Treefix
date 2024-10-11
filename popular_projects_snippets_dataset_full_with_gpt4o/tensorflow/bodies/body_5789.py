# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
devices = [
    '/job:tpu_worker/task:0/device:CPU:0',
    '/job:tpu_worker/task:1/device:CPU:0',
    '/job:tpu_worker/task:2/device:CPU:0',
    '/job:tpu_worker/task:3/device:CPU:0',
    '/job:tpu_worker/task:0/device:GPU:1',
    '/job:tpu_worker/task:1/device:GPU:1',
    '/job:tpu_worker/task:2/device:GPU:1',
    '/job:tpu_worker/task:3/device:GPU:1',
]
device_list = [
    session._DeviceAttributes(name, 'XLA', 1024, 0) for name in devices
]

device_dict, num_cores =\
        resolver.TPUClusterResolver._get_device_dict_and_cores(device_list)
self.assertEqual(num_cores, 0)
self.assertEqual(device_dict, {})
