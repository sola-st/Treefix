# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
assert context.executing_eagerly()
logdir = self.get_temp_dir()
writer = summary_ops.create_file_writer_v2(logdir)
with writer.as_default():
    summary_op_fn()
writer.close()
events = events_from_logdir(logdir)
exit(events[1])
