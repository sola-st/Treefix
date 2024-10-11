# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
dispatcher = server_lib.DispatchServer()
worker = server_lib.WorkerServer(
    server_lib.WorkerConfig(dispatcher._address))
# Test the profilers are successfully started and connected to profiler
# service on the worker. Since there is no op running, it is expected to
# return UnavailableError with no trace events collected string.
with self.assertRaises(errors.UnavailableError) as error:
    profiler_client.trace(worker._address, tempfile.mkdtemp(), duration_ms=10)
self.assertStartsWith(str(error.exception), "No trace event was collected")
