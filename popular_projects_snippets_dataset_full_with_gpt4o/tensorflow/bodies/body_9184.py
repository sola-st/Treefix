# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
"""Test single worker sampling mode."""

def on_worker(port, worker_start):
    logging.info('worker starting server on {}'.format(port))
    profiler.start_server(port)
    _, steps, train_ds, model = _model_setup()
    worker_start.set()
    while True:
        model.fit(x=train_ds, epochs=2, steps_per_epoch=steps)
        if self.profile_done:
            break

def on_profile(port, logdir, worker_start):
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

logdir = self.get_temp_dir()
port = portpicker.pick_unused_port()
thread_profiler = threading.Thread(
    target=on_profile, args=(port, logdir, self.worker_start))
thread_worker = threading.Thread(
    target=on_worker, args=(port, self.worker_start))
thread_worker.start()
thread_profiler.start()
thread_profiler.join()
thread_worker.join(120)
self._check_xspace_pb_exist(logdir)
