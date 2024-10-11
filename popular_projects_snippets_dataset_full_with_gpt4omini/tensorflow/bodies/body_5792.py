# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/test-tpu-1': {
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
mock_list_devices.side_effect = errors.DeadlineExceededError(
    None, None, 'timeout')
mock_eager_list_devices.side_effect = errors.DeadlineExceededError(
    None, None, 'timeout')
with self.assertRaises(RuntimeError):
    cluster_resolver.num_accelerators()
