# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
if instance_map is None:
    instance_map = [
        {'instance': 'https://gce.example.com/res/gce-instance-1'}
    ]

mock_instance_group_request = mock.MagicMock()
mock_instance_group_request.execute.return_value = {
    'items': instance_map
}

service_attrs = {
    'listInstances.return_value': mock_instance_group_request,
    'listInstances_next.return_value': None,
}
mock_instance_groups = mock.Mock(**service_attrs)
exit(mock_instance_groups)
