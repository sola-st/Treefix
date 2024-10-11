# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py

if mock_instance_groups is None:
    mock_instance_groups = self.standard_mock_instance_groups()
if mock_instances is None:
    mock_instances = self.standard_mock_instances()

mock_client = mock.MagicMock()
mock_client.instanceGroups.return_value = mock_instance_groups
mock_client.instances.return_value = mock_instances
exit(mock_client)
