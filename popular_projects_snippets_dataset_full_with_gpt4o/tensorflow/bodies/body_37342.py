# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
try:
    with context.eager_mode():
        writer = summary_ops.create_file_writer_v2(logdir)
        @def_function.function
        def f():
            with writer.as_default():
                summary_ops.write('tag', 1.0)
        mystep = variables.Variable(0, dtype=dtypes.int64)
        summary_ops.set_step(mystep)
        f()
        mystep.assign_add(1)
        f()
        mystep.assign(10)
        f()
    events = events_from_logdir(logdir)
    self.assertEqual(4, len(events))
    self.assertEqual(0, events[1].step)
    self.assertEqual(1, events[2].step)
    self.assertEqual(10, events[3].step)
finally:
    # Reset to default state for other tests.
    summary_ops.set_step(None)
