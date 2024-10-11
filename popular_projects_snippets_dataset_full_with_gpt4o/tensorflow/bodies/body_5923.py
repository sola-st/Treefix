# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
worker1_name_to_ip = [
    {'name': 'instance1', 'ip': '10.1.2.3'},
    {'name': 'instance2', 'ip': '10.2.3.4'},
    {'name': 'instance3', 'ip': '10.3.4.5'},
]

worker2_name_to_ip = [
    {'name': 'instance4', 'ip': '10.4.5.6'},
    {'name': 'instance5', 'ip': '10.5.6.7'},
    {'name': 'instance6', 'ip': '10.6.7.8'},
]

ps_name_to_ip = [
    {'name': 'ps1', 'ip': '10.100.1.2'},
    {'name': 'ps2', 'ip': '10.100.2.3'},
]

worker1_gce_cluster_resolver = GCEClusterResolver(
    project='test-project',
    zone='us-east1-d',
    instance_group='test-instance-group',
    task_type='worker',
    port=8470,
    credentials=None,
    service=self.gen_standard_mock_service_client(worker1_name_to_ip))

worker2_gce_cluster_resolver = GCEClusterResolver(
    project='test-project',
    zone='us-east1-d',
    instance_group='test-instance-group',
    task_type='worker',
    port=8470,
    credentials=None,
    service=self.gen_standard_mock_service_client(worker2_name_to_ip))

ps_gce_cluster_resolver = GCEClusterResolver(
    project='test-project',
    zone='us-east1-d',
    instance_group='test-instance-group',
    task_type='ps',
    port=2222,
    credentials=None,
    service=self.gen_standard_mock_service_client(ps_name_to_ip))

union_cluster_resolver = UnionClusterResolver(worker1_gce_cluster_resolver,
                                              worker2_gce_cluster_resolver,
                                              ps_gce_cluster_resolver)

actual_cluster_spec = union_cluster_resolver.cluster_spec()
expected_proto = """
    job { name: 'ps' tasks { key: 0 value: '10.100.1.2:2222' }
                     tasks { key: 1 value: '10.100.2.3:2222' } }
    job { name: 'worker' tasks { key: 0 value: '10.1.2.3:8470' }
                         tasks { key: 1 value: '10.2.3.4:8470' }
                         tasks { key: 2 value: '10.3.4.5:8470' }
                         tasks { key: 3 value: '10.4.5.6:8470' }
                         tasks { key: 4 value: '10.5.6.7:8470' }
                         tasks { key: 5 value: '10.6.7.8:8470' } }
    """
self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)
