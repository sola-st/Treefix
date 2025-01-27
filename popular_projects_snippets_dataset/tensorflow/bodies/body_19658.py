# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
"""Return a list of tpu endpoints."""
if not self._use_api:
    exit(list(_environment_var_to_network_endpoints(self._tpu)))
response = self._fetch_cloud_tpu_metadata()

if response.get('state') != 'READY':
    raise RuntimeError('TPU "%s" is not yet ready; state: "%s"' %
                       (self._tpu, response.get('state')))
if 'networkEndpoints' in response:
    exit(response['networkEndpoints'])
else:
    exit([{'ipAddress': response['ipAddress'], 'port': response['port']}])
