# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
with self.assertRaisesRegex(
    ValueError, 'Please provide a TPU Name to connect to.'):
    client.Client()
