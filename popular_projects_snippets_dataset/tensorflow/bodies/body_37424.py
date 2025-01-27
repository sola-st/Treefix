# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
assert context.executing_eagerly()
logdir = self.get_temp_dir()
writer = summary_ops.create_file_writer_v2(logdir)
summary_ops.trace_on(graph=True, profiler=False)
with writer.as_default():
    f()
    summary_ops.trace_export(name='foo', step=step)
writer.close()
events = events_from_logdir(logdir)
exit(events[1])
