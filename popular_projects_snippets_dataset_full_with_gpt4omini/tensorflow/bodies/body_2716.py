# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
super(DLPackTest, self).setUp()
self.backend = xla_backend()
if self.backend.platform not in ("cpu", "gpu"):
    self.skipTest("DLPack requires CPU or GPU")
self.cpu_backend = (
    self.backend
    if self.backend.platform == "cpu" else xla_client.make_cpu_client())
self.gpu_backend = (
    self.backend if self.backend.platform == "gpu" else None)
