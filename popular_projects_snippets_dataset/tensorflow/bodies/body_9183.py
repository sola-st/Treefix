# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
# Request for 30 milliseconds of profile.
duration_ms = 30

worker_start.wait()
options = profiler.ProfilerOptions(
    host_tracer_level=2,
    python_tracer_level=0,
    device_tracer_level=1,
    delay_ms=delay_ms,
)

profiler_client.trace('localhost:{}'.format(port), logdir, duration_ms,
                      '', 100, options)

self.profile_done = True
