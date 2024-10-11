# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_client_test.py
# Monitor is only supported in cloud TPU. Test invalid address instead.
with self.assertRaises(errors.UnavailableError):
    profiler_client.monitor('localhost:6006', 2000)
