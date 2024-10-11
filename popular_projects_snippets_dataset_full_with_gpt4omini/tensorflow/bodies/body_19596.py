# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
os.environ['TPU_API_DISCOVERY_URL'] = 'https://{api}.internal/{apiVersion}'
self.assertEqual('https://{api}.internal/{apiVersion}',
                 (client._environment_discovery_url()))
