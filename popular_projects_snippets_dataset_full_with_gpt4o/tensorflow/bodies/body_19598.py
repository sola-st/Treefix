# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
self.assertEqual(
    [{'ipAddress': '1.2.3.4', 'port': '2000'}],
    list(
        client._environment_var_to_network_endpoints(
            'grpc://1.2.3.4:2000')))
