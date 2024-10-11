# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
super().setUp()
self.worker_start = threading.Event()
self.profile_done = False
