# Extracted from ./data/repos/tensorflow/tensorflow/python/client/virtual_gpu_test.py
with self.session(config=self._util.config) as sess:
    # TODO(laigd): b/70811538. The is_gpu_available() call will invoke
    # DeviceFactory::AddDevices() with a default SessionOption, which prevents
    # adding virtual devices in the future, thus must be called within a
    # context of a session within which virtual devices are created. Same in
    # the following test case.
    if not test.is_gpu_available(cuda_only=True):
        self.skipTest('No GPU available')
    run_options = config_pb2.RunOptions(
        trace_level=config_pb2.RunOptions.FULL_TRACE)
    run_metadata = config_pb2.RunMetadata()

    mat_shape = [10, 10]
    data = []
    for d in self._util.devices:
        with ops.device(d):
            var = variables.Variable(random_ops.random_uniform(mat_shape))
            self.evaluate(var.initializer)
            data.append(var)
    s = data[0]
    for i in range(1, len(data)):
        s = math_ops.add(s, data[i])
    sess.run(s, options=run_options, run_metadata=run_metadata)

self.assertTrue(run_metadata.HasField('step_stats'))
step_stats = run_metadata.step_stats
devices = [d.device for d in step_stats.dev_stats]
self.assertTrue('/job:localhost/replica:0/task:0/device:CPU:0' in devices)
self.assertTrue('/job:localhost/replica:0/task:0/device:GPU:0' in devices)
self.assertTrue('/job:localhost/replica:0/task:0/device:GPU:1' in devices)
self.assertTrue('/job:localhost/replica:0/task:0/device:GPU:2' in devices)
