# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
"""Test single worker without profiling."""

_, steps, train_ds, model = _model_setup()

model.fit(x=train_ds, epochs=2, steps_per_epoch=steps)
