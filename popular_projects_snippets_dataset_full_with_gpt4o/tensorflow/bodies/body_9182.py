# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
logging.info('worker starting server on {}'.format(port))
profiler.start_server(port)
_, steps, train_ds, model = _model_setup()
worker_start.set()
while True:
    model.fit(x=train_ds, epochs=2, steps_per_epoch=steps)
    if self.profile_done:
        break
