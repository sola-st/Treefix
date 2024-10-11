# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline_test.py
run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata = config_pb2.RunMetadata()
config = config_pb2.ConfigProto(device_count={'CPU': 3})
with session.Session(config=config) as sess:
    with ops.device('/cpu:0'):
        num1 = variables.Variable(1.0, name='num1')
    with ops.device('/cpu:1'):
        num2 = variables.Variable(2.0, name='num2')
    with ops.device('/cpu:2'):
        result = num1 + num2 + num1 * num2
    self.evaluate(variables.global_variables_initializer())
    sess.run(result, options=run_options, run_metadata=run_metadata)
self.assertTrue(run_metadata.HasField('step_stats'))
step_stats = run_metadata.step_stats
devices = [d.device for d in step_stats.dev_stats]
self.assertTrue('/job:localhost/replica:0/task:0/device:CPU:0' in devices)
self.assertTrue('/job:localhost/replica:0/task:0/device:CPU:1' in devices)
self.assertTrue('/job:localhost/replica:0/task:0/device:CPU:2' in devices)
tl = timeline.Timeline(step_stats)
ctf = tl.generate_chrome_trace_format()
self._validateTrace(ctf)
tl = timeline.Timeline(step_stats)
ctf = tl.generate_chrome_trace_format(show_dataflow=False)
self._validateTrace(ctf)
tl = timeline.Timeline(step_stats)
ctf = tl.generate_chrome_trace_format(show_memory=False)
self._validateTrace(ctf)
tl = timeline.Timeline(step_stats)
ctf = tl.generate_chrome_trace_format(
    show_memory=False, show_dataflow=False)
self._validateTrace(ctf)
