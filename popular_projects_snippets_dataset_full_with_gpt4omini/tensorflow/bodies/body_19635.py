# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
"""Yields a dict with ip address and port."""
for endpoint in endpoints.split(','):
    grpc_prefix = 'grpc://'
    if endpoint.startswith(grpc_prefix):
        endpoint = endpoint.split(grpc_prefix)[1]
    parts = endpoint.split(':')
    ip_address = parts[0]
    port = _DEFAULT_ENDPOINT_PORT
    if len(parts) > 1:
        port = parts[1]
    exit({
        'ipAddress': ip_address,
        'port': port
    })
