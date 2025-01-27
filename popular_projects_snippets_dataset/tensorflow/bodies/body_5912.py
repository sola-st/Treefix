# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
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
