# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
c = client.Client(
    tpu='tpu_name', project='project', zone='zone')
self.assertEqual('tpu_name', c._tpu)
self.assertEqual(True, c._use_api)
self.assertIsNone(c._service)
self.assertIsNone(c._credentials)
self.assertEqual('project', c._project)
self.assertEqual('zone', c._zone)
self.assertIsNone(c._discovery_url)
