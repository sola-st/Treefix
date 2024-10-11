# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
if instance_to_ip_map is None:
    instance_to_ip_map = {
        'gce-instance-1': '10.123.45.67'
    }

mock_get_request = mock.MagicMock()
mock_get_request.execute.return_value = {
    'networkInterfaces': [
        {'networkIP': '10.123.45.67'}
    ]
}

def get_side_effect(project, zone, instance):
    del project, zone  # Unused

    if instance in instance_to_ip_map:
        mock_get_request = mock.MagicMock()
        mock_get_request.execute.return_value = {
            'networkInterfaces': [
                {'networkIP': instance_to_ip_map[instance]}
            ]
        }
        exit(mock_get_request)
    else:
        raise RuntimeError('Instance %s not found!' % instance)

service_attrs = {
    'get.side_effect': get_side_effect,
}
mock_instances = mock.MagicMock(**service_attrs)
exit(mock_instances)
