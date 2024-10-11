# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
try:
    with context.eager_mode():
        with summary_ops.create_file_writer_v2(logdir).as_default():
            summary_ops.set_step(1)
            summary_ops.write('tag', 1.0)
            summary_ops.set_step(2)
            summary_ops.write('tag', 1.0)
            mystep = variables.Variable(10, dtype=dtypes.int64)
            summary_ops.set_step(mystep)
            summary_ops.write('tag', 1.0)
            mystep.assign_add(1)
            summary_ops.write('tag', 1.0)
    events = events_from_logdir(logdir)
    self.assertEqual(5, len(events))
    self.assertEqual(1, events[1].step)
    self.assertEqual(2, events[2].step)
    self.assertEqual(10, events[3].step)
    self.assertEqual(11, events[4].step)
finally:
    # Reset to default state for other tests.
    summary_ops.set_step(None)
