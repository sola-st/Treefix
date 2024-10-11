# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/test-tpu-1': {
        'ipAddress': '10.1.2.3',
        'port': '8470',
        'state': 'CREATING'
    }
}

cluster_resolver = resolver.TPUClusterResolver(
    project=None,
    zone=None,
    tpu='test-tpu-1',
    coordinator_name=None,
    credentials=None,
    service=self.mock_service_client(tpu_map=tpu_map))

with self.assertRaises(RuntimeError):
    cluster_resolver.cluster_spec()
