# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
"""Test single worker programmatic mode."""
logdir = self.get_temp_dir()

options = profiler.ProfilerOptions(
    host_tracer_level=2,
    python_tracer_level=0,
    device_tracer_level=1,
)
profiler.start(logdir, options)
_, steps, train_ds, model = _model_setup()
model.fit(x=train_ds, epochs=2, steps_per_epoch=steps)
profiler.stop()
self._check_xspace_pb_exist(logdir)
