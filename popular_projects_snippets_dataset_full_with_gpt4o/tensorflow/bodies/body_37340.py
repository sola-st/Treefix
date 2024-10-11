# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
try:
    with context.eager_mode():
        writer = summary_ops.create_file_writer_v2(logdir)
        @def_function.function
        def f():
            with writer.as_default():
                summary_ops.write('tag', 1.0)
        summary_ops.set_step(1)
        f()
        summary_ops.set_step(2)
        f()
    events = events_from_logdir(logdir)
    self.assertEqual(3, len(events))
    self.assertEqual(1, events[1].step)
    # The step value will still be 1 because the value was captured at the
    # time the function was first traced.
    self.assertEqual(1, events[2].step)
finally:
    # Reset to default state for other tests.
    summary_ops.set_step(None)
