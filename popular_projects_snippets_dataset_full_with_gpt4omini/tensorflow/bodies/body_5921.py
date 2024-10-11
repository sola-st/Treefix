# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
gce_cluster_resolver = GCEClusterResolver(
    project='test-project',
    zone='us-east1-d',
    instance_group='test-instance-group',
    task_type='custom',
    port=2222,
    credentials=None,
    service=self.standard_mock_service_client())

actual_cluster_spec = gce_cluster_resolver.cluster_spec()
expected_proto = """
    job { name: 'custom' tasks { key: 0 value: '10.123.45.67:2222' } }
    """
self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)
