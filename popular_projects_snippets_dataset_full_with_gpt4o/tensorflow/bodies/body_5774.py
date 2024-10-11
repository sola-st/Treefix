# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/test-tpu-1': {
        'state': 'READY',
        'health': 'HEALTHY',
        'networkEndpoints': [{
            'ipAddress': '10.2.3.4',
            'port': 8470,
        }]
    }
}

cluster_resolver = resolver.TPUClusterResolver(
    project='test-project',
    zone='us-central1-c',
    tpu='test-tpu-1',
    coordinator_name='coordinator',
    coordinator_address='10.128.1.5:10203',
    credentials=None,
    service=self.mock_service_client(tpu_map=tpu_map))

actual_cluster_spec = cluster_resolver.cluster_spec()
expected_proto = """
    job { name: 'coordinator' tasks { key: 0 value: '10.128.1.5:10203' } }
    job { name: 'worker' tasks { key: 0 value: '10.2.3.4:8470' } }
    """
self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)
self.assertEqual('grpc://10.2.3.4:8470', cluster_resolver.master())
