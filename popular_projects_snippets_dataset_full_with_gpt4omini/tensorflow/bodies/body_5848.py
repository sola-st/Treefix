# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver_test.py
mock_client = mock.MagicMock()
mock_client.list_pod_for_all_namespaces.side_effect = (
    lambda *args, **kwargs: ret[kwargs['label_selector']])
exit(mock_client)
