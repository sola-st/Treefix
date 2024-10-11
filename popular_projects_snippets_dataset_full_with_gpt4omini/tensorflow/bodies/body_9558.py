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
tl = timeline.Timeline(run_metadata.step_stats)
step_analysis = tl.analyze_step_stats()
ctf = step_analysis.chrome_trace.format_to_string()
self._validateTrace(ctf)
maximums = step_analysis.allocator_maximums
cpuname = 'mklcpu' if test_util.IsMklEnabled() else 'cpu'
self.assertTrue(cpuname in maximums)
cpu_max = maximums[
    'cuda_host_bfc'] if 'cuda_host_bfc' in maximums else maximums[cpuname]
# At least num1 + num2, both float32s (4 bytes each)
self.assertGreaterEqual(cpu_max.num_bytes, 8)
self.assertGreater(cpu_max.timestamp, 0)
