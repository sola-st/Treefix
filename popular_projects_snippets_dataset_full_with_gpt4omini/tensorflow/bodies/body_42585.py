# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/profiler_client_test.py
with self.assertRaises(errors.UnavailableError):
    profiler_client.start_tracing('localhost:6006', '/tmp/', 2000)
