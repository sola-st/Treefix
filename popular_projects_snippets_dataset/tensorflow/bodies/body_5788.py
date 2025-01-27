# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
devices = [
    '/job:tpu_worker/task:0/device:TPU:0',
    '/job:tpu_worker/task:1/device:TPU:1',
    '/job:tpu_worker/task:2/device:TPU:0',
    '/job:tpu_worker/task:3/device:TPU:1',
    '/job:tpu_worker/task:0/device:TPU:4',
    '/job:tpu_worker/task:1/device:TPU:5',
    '/job:tpu_worker/task:2/device:TPU:4',
    '/job:tpu_worker/task:3/device:TPU:5',
]
device_list = [
    session._DeviceAttributes(name, 'TPU', 1024, 0) for name in devices
]

device_details = resolver.TPUClusterResolver._get_device_dict_and_cores(
    device_list)
self.assertEqual(device_details.total_cores, 8)
self.assertEqual(device_details.device_map,
                 {'0': ['0', '4'],
                  '1': ['1', '5'],
                  '2': ['0', '4'],
                  '3': ['1', '5']})
