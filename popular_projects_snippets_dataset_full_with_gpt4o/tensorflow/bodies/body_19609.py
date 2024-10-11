# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
c = client.Client(tpu='grpc://1.2.3.4:8470')
self.assertEqual('grpc://1.2.3.4:8470', c._tpu)
self.assertEqual(False, c._use_api)
self.assertIsNone(c._service)
self.assertIsNone(c._credentials)
self.assertIsNone(c._project)
self.assertIsNone(c._zone)
self.assertIsNone(c._discovery_url)
self.assertEqual([{
    'ipAddress': '1.2.3.4',
    'port': '8470'
}], c.network_endpoints())
