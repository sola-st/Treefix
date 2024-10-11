# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
devices = [
    LogicalDevice('/job:tpu_worker/task:0/device:TPU:0', 'TPU'),
    LogicalDevice('/job:tpu_worker/task:1/device:TPU:1', 'TPU'),
    LogicalDevice('/job:tpu_worker/task:2/device:TPU:0', 'TPU'),
    LogicalDevice('/job:tpu_worker/task:3/device:TPU:1', 'TPU'),
    LogicalDevice('/job:tpu_worker/task:0/device:TPU:4', 'TPU'),
    LogicalDevice('/job:tpu_worker/task:1/device:TPU:5', 'TPU'),
    LogicalDevice('/job:tpu_worker/task:2/device:TPU:4', 'TPU'),
    LogicalDevice('/job:tpu_worker/task:3/device:TPU:5', 'TPU'),
]
device_list = [
    session._DeviceAttributes(d.name, d.device_type, 1024, 0)
    for d in devices
]
mock_eager_list_devices.return_value = devices
mock_list_devices.return_value = device_list

tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/test-tpu-1': {
        'state': 'READY',
        'health':
            'HEALTHY',
        'networkEndpoints': [
            {
                'ipAddress': '10.2.3.4',
                'port': 8470,
            },
            {
                'ipAddress': '10.2.3.5',
                'port': 8470,
            },
            {
                'ipAddress': '10.2.3.6',
                'port': 8470,
            },
            {
                'ipAddress': '10.2.3.7',
                'port': 8470,
            },
        ]
    }
}

cluster_resolver = resolver.TPUClusterResolver(
    project='test-project',
    zone='us-central1-c',
    tpu='test-tpu-1',
    service=self.mock_service_client(tpu_map=tpu_map))
self.assertEqual(cluster_resolver.num_accelerators(), {'TPU': 2})
