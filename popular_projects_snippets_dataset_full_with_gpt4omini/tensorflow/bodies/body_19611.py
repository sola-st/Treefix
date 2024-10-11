# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
c = client.Client(tpu='grpc://1.2.3.4:8470')
self.assertEqual(True, c.recoverable())
