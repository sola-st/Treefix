# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_client_test.py
test_port = portpicker.pick_unused_port()
profiler.start_server(test_port)
# Test the profilers are successfully started and connected to profiler
# service on the worker. Since there is no op running, it is expected to
# return UnavailableError with no trace events collected string.
with self.assertRaises(errors.UnavailableError) as error:
    options = profiler.ProfilerOptions(
        host_tracer_level=3, device_tracer_level=0)
    profiler_client.trace(
        'localhost:' + str(test_port),
        self.get_temp_dir(),
        duration_ms=10,
        options=options)
self.assertStartsWith(str(error.exception), 'No trace event was collected')
