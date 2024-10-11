# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/test-tpu-1': {
        'ipAddress': '10.1.2.3',
        'port': '8470',
        'state': 'READY',
        'health': 'HEALTHY'
    }
}

cluster_resolver = resolver.TPUClusterResolver(
    project=None,
    zone=None,
    tpu=['test-tpu-1'],
    credentials=None,
    service=self.mock_service_client(tpu_map=tpu_map),
    coordinator_name='coordinator')

actual_cluster_spec = cluster_resolver.cluster_spec()
expected_proto = """
    job {
      name: 'coordinator'
      tasks { key: 0 value: '10.128.1.2:%s' }
    }
    job {
      name: 'worker'
      tasks { key: 0 value: '10.1.2.3:8470' }
    }
    """ % cluster_resolver._coordinator_port
self._verifyClusterSpecEquality(actual_cluster_spec, str(expected_proto))
self.assertEqual(cluster_resolver.master(), 'grpc://10.1.2.3:8470')
