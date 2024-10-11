# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
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
    coordinator_name=None,
    credentials=None,
    service=self.mock_service_client(tpu_map=tpu_map))

self.assertEqual(cluster_resolver.master(), 'grpc://10.2.3.4:8470')

cluster_resolver.task_type = 'worker'
cluster_resolver.task_id = 3
self.assertEqual(cluster_resolver.master(), 'grpc://10.2.3.7:8470')
