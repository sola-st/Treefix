# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
# TODO(phawkins): These tests just check that the TraceMe context manager
# acts like a context manager and doesn't explode. Ideally we'd check that
# the profiler saw the traceme too.
with xla_client.profiler.TraceMe("test1"):
    pass
with xla_client.profiler.TraceMe("test2", foo=123):
    pass
with self.assertRaises(ValueError):
    with xla_client.profiler.TraceMe("test3"):
        raise ValueError("test")
