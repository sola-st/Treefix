# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver_test.py
os.environ['TF_CONFIG'] = """
    {
      "cluster": {
        "worker1": ["w10:2222"],
        "worker2": ["w21:2222", "w22:2222", "w23:2222", "w24:2222"]
      },
      "rpc_layer": "grpc",
      "task": {
        "type": "worker1",
        "index": "0"
      }
    }
    """

devices = [
    LogicalDevice('/job:worker1/task:0/device:TPU:0', 'TPU'),
    LogicalDevice('/job:worker1/task:0/device:TPU:1', 'TPU'),
    LogicalDevice('/job:worker1/task:0/device:GPU:0', 'GPU'),
    LogicalDevice('/job:worker1/task:0/device:GPU:1', 'GPU'),
    LogicalDevice('/job:worker2/task:1/device:TPU:2', 'TPU'),
    LogicalDevice('/job:worker2/task:2/device:TPU:3', 'TPU'),
    LogicalDevice('/job:worker2/task:3/device:GPU:2', 'GPU'),
    LogicalDevice('/job:worker2/task:4/device:GPU:3', 'GPU'),
]
device_list = [
    session._DeviceAttributes(d.name, d.device_type, 1024, 0)
    for d in devices
]
mock_eager_list_devices.return_value = devices
mock_list_devices.return_value = device_list

resolver = TFConfigClusterResolver()

# By default we read from TF_CONFIG
self.assertEqual(resolver.num_accelerators(), {'TPU': 2, 'GPU': 2})

# Override still works when we want it to
self.assertEqual(resolver.num_accelerators(task_type='worker2', task_id=3),
                 {'GPU': 1})
