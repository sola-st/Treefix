# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
self.assertEqual(
    client.Client(
        tpu='tpu_name', zone='zone', project='project')._full_name(),
    client.Client(
        tpu=b'tpu_name', zone=b'zone', project=b'project')._full_name(),
)
