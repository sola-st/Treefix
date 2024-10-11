# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
with self.assertRaisesRegex(
    NotImplementedError,
    'Using multiple TPUs in a single session is not yet implemented'):
    client.Client(tpu=['multiple', 'elements'])
