# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver_test.py
ret = _create_pod_list(
    ('worker-0', 'Running', '10.1.2.3'),
    ('worker-1', 'Running', '10.1.2.4'),
    ('worker-2', 'Running', '10.1.2.5'))

cluster_resolver = KubernetesClusterResolver(
    override_client=_mock_kubernetes_client(
        {'job-name=tensorflow': ret}))
cluster_resolver.task_type = 'worker'
cluster_resolver.task_id = 0
self.assertEqual(cluster_resolver.task_type, 'worker')
self.assertEqual(cluster_resolver.task_id, 0)
self.assertEqual(cluster_resolver.master(), 'grpc://10.1.2.3:8470')
self.assertEqual(cluster_resolver.master('worker', 2),
                 'grpc://10.1.2.5:8470')
