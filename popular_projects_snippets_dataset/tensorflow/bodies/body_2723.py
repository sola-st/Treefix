# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
super(BufferProtocolTest, self).setUp()
self.backend = xla_backend()
if self.backend.platform != "cpu":
    self.skipTest("Test requires CPU")
