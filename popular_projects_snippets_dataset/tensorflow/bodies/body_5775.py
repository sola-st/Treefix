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
    tpu='test-tpu-1',
    credentials=None,
    service=self.mock_service_client(tpu_map=tpu_map),
    coordinator_name='coordinator')

actual_cluster_spec = cluster_resolver.cluster_spec()
expected_proto = """
    job {
      name: 'coordinator',
      tasks { key: 0 value: '10.128.1.2:%s'}
    }
    job {
      name: 'worker'
      tasks { key: 0 value: '10.2.3.4:8470' }
      tasks { key: 1 value: '10.2.3.5:8470' }
      tasks { key: 2 value: '10.2.3.6:8470' }
      tasks { key: 3 value: '10.2.3.7:8470' }
    }
    """ % cluster_resolver._coordinator_port
self._verifyClusterSpecEquality(actual_cluster_spec, str(expected_proto))
self.assertEqual(cluster_resolver.master(), 'grpc://10.2.3.4:8470')
