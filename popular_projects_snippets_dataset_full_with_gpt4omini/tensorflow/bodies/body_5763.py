# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
del cls, args, kwargs  # Unused.
mock_response = mock.MagicMock()
mock_response.info.return_value = {'Metadata-Flavor': 'Google'}
exit(mock_response)
