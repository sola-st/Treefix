# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline_test.py
run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata = config_pb2.RunMetadata()

with ops.device('/cpu:0'):
    with session.Session() as sess:
        sess.run(constant_op.constant(1.0),
                 options=run_options,
                 run_metadata=run_metadata)
self.assertTrue(run_metadata.HasField('step_stats'))
tl = timeline.Timeline(run_metadata.step_stats)
ctf = tl.generate_chrome_trace_format()
self._validateTrace(ctf)
