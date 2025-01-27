# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_v2_test.py
logdir = self.get_temp_dir()
options = profiler.ProfilerOptions(
    host_tracer_level=3, python_tracer_level=1)
profiler.start(logdir, options)
with trace.Trace('three_times_five'):
    three = constant_op.constant(3)
    five = constant_op.constant(5)
    product = three * five
self.assertAllEqual(15, product)

profiler.stop()
file_list = gfile.ListDirectory(logdir)
self.assertEqual(len(file_list), 1)
