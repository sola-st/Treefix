# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
self.assertEqual('tpu_name', c._tpu)
self.assertEqual(True, c._use_api)
self.assertIsNone(c._credentials)
self.assertEqual('test-project', c._project)
self.assertEqual('us-central1-c', c._zone)
self.assertIsNone(c._discovery_url)
self.assertEqual([{
    'ipAddress': '10.1.2.3',
    'port': '8470'
}], c.network_endpoints())
