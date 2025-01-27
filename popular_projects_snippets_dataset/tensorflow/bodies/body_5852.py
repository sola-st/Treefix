# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver_test.py
ret = _create_pod_list(('tensorflow-abc123', 'Running', '10.1.2.3'),)

cluster_resolver = KubernetesClusterResolver(
    override_client=_mock_kubernetes_client(
        {'job-name=tensorflow': ret}))

actual_cluster_spec = cluster_resolver.cluster_spec()
expected_proto = """
    job {
      name: 'worker'
      tasks { key: 0 value: '10.1.2.3:8470' }
    }
    """
self._verifyClusterSpecEquality(actual_cluster_spec, str(expected_proto))
