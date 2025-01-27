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
    task_type='testworker',
    port=8470,
    credentials=None,
    service=self.gen_standard_mock_service_client(name_to_ip))

gce_cluster_resolver.task_id = 1
gce_cluster_resolver.rpc_layer = 'test'

self.assertEqual(gce_cluster_resolver.task_type, 'testworker')
self.assertEqual(gce_cluster_resolver.task_id, 1)
self.assertEqual(gce_cluster_resolver.rpc_layer, 'test')
self.assertEqual(gce_cluster_resolver.master(), 'test://10.2.3.4:8470')
