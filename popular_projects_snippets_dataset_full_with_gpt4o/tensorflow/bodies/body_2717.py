# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
super().tearDown()
del self.backend
del self.cpu_backend
del self.gpu_backend
