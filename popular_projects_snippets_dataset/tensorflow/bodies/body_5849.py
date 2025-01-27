# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver_test.py
mock_status = mock.Mock()
mock_status.configure_mock(phase=phase, host_ip=host_ip)

mock_metadata = mock.Mock()
mock_metadata.configure_mock(name=name)

mock_item = mock.Mock()
mock_item.configure_mock(status=mock_status, metadata=mock_metadata)
exit(mock_item)
