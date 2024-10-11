# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
gce_cluster_resolver = GCEClusterResolver(
    project='test-project',
    zone='us-east1-d',
    instance_group='test-instance-group',
    task_id=0,
    port=8470,
    credentials=None,
    service=self.standard_mock_service_client())
self.assertEqual(gce_cluster_resolver.master(), 'grpc://10.123.45.67:8470')
