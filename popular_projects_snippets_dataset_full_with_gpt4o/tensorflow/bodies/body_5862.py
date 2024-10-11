# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver_test.py
devices = [
    LogicalDevice("/job:worker1/task:0/device:TPU:0", "TPU"),
    LogicalDevice("/job:worker1/task:0/device:TPU:1", "TPU"),
    LogicalDevice("/job:worker1/task:0/device:GPU:0", "GPU"),
    LogicalDevice("/job:worker1/task:0/device:GPU:1", "GPU"),
    LogicalDevice("/job:worker2/task:1/device:TPU:2", "TPU"),
    LogicalDevice("/job:worker2/task:2/device:TPU:3", "TPU"),
    LogicalDevice("/job:worker2/task:3/device:GPU:2", "GPU"),
    LogicalDevice("/job:worker2/task:4/device:GPU:3", "GPU"),
]
device_list = [
    session._DeviceAttributes(d.name, d.device_type, 1024, 0)
    for d in devices
]
mock_eager_list_devices.return_value = devices
mock_list_devices.return_value = device_list

resolver = MockBaseClusterResolver()
self.assertEqual(resolver.num_accelerators(task_type="worker1", task_id=0),
                 {"TPU": 2, "GPU": 2})
self.assertEqual(resolver.num_accelerators(task_type="worker2", task_id=3),
                 {"GPU": 1})
self.assertEqual(resolver.num_accelerators(task_type="worker2", task_id=4),
                 {"GPU": 1})
