# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver_test.py
ret = _create_pod_list(('tensorflow-abc123', 'Failed', '10.1.2.3'),)

cluster_resolver = KubernetesClusterResolver(
    override_client=_mock_kubernetes_client(
        {'job-name=tensorflow': ret}))

error_msg = 'Pod "tensorflow-abc123" is not running; phase: "Failed"'
with self.assertRaisesRegex(RuntimeError, error_msg):
    cluster_resolver.cluster_spec()
