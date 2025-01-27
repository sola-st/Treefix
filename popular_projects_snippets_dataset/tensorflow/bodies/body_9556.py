# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline_test.py
if not test.is_gpu_available(cuda_only=True):
    exit()

run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata = config_pb2.RunMetadata()

with self.session(force_gpu=True) as sess:
    const1 = constant_op.constant(1.0, name='const1')
    const2 = constant_op.constant(2.0, name='const2')
    result = math_ops.add(const1, const2) + const1 * const2
    sess.run(result, options=run_options, run_metadata=run_metadata)
self.assertTrue(run_metadata.HasField('step_stats'))
step_stats = run_metadata.step_stats
devices = [d.device for d in step_stats.dev_stats]
self.assertTrue('/job:localhost/replica:0/task:0/device:GPU:0' in devices)
self.assertIn('/device:GPU:0/stream:all', devices)
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
