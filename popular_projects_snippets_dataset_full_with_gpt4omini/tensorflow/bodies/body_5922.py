# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
name_to_ip = [
    {'name': 'instance1', 'ip': '10.1.2.3'},
    {'name': 'instance2', 'ip': '10.2.3.4'},
    {'name': 'instance3', 'ip': '10.3.4.5'},
]

gce_cluster_resolver = GCEClusterResolver(
    project='test-project',
    zone='us-east1-d',
    instance_group='test-instance-group',
    port=8470,
    credentials=None,
    service=self.gen_standard_mock_service_client(name_to_ip))

actual_cluster_spec = gce_cluster_resolver.cluster_spec()
expected_proto = """
    job { name: 'worker' tasks { key: 0 value: '10.1.2.3:8470' }
                         tasks { key: 1 value: '10.2.3.4:8470' }
                         tasks { key: 2 value: '10.3.4.5:8470' } }
    """
self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)
