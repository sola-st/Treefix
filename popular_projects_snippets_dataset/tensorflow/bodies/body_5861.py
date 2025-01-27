# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver_test.py
devices = [
    LogicalDevice("/job:worker/task:0/device:TPU:0", "TPU"),
    LogicalDevice("/job:worker/task:0/device:TPU:1", "TPU"),
    LogicalDevice("/job:worker/task:0/device:TPU:2", "TPU"),
    LogicalDevice("/job:worker/task:0/device:TPU:3", "TPU"),
    LogicalDevice("/job:worker/task:0/device:GPU:0", "GPU"),
    LogicalDevice("/job:worker/task:0/device:GPU:1", "GPU"),
    LogicalDevice("/job:worker/task:0/device:GPU:2", "GPU"),
    LogicalDevice("/job:worker/task:0/device:GPU:3", "GPU"),
]
device_list = [
    session._DeviceAttributes(d.name, d.device_type, 1024, 0)
    for d in devices
]
mock_eager_list_devices.return_value = devices
mock_list_devices.return_value = device_list

resolver = MockBaseClusterResolver()
self.assertEqual(resolver.num_accelerators(), {"TPU": 4, "GPU": 4})
