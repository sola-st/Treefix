# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py

if tpu_map is None:
    tpu_map = {}

mock_locations = mock.MagicMock()
mock_locations.nodes.return_value = MockNodeClass(tpu_map)

mock_project = mock.MagicMock()
mock_project.locations.return_value = mock_locations

mock_client = mock.MagicMock()
mock_client.projects.return_value = mock_project

exit(mock_client)
