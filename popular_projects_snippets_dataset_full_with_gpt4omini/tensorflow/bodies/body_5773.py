# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/test-tpu-1': {
        'ipAddress': '10.1.2.3',
        'port': '8470',
        'health': 'HEALTHY'
    }
}

cluster_resolver = resolver.TPUClusterResolver(
    project='test-project',
    zone='us-central1-c',
    tpu='nonexistent-tpu',
    coordinator_name='coordinator',
    coordinator_address='10.128.1.5:10203',
    credentials=None,
    service=self.mock_service_client(tpu_map=tpu_map))

with self.assertRaises(ValueError) as context:
    cluster_resolver.cluster_spec()

self.assertIn('Could not lookup TPU metadata', str(context.exception))
