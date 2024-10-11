# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
try:
    with context.eager_mode():
        writer = summary_ops.create_file_writer_v2(logdir)
        with writer.as_default(step=1):
            summary_ops.write('tag', 1.0)
            with writer.as_default():
                summary_ops.write('tag', 1.0)
                with writer.as_default(step=2):
                    summary_ops.write('tag', 1.0)
                summary_ops.write('tag', 1.0)
                summary_ops.set_step(3)
            summary_ops.write('tag', 1.0)
    events = events_from_logdir(logdir)
    self.assertListEqual([1, 1, 2, 1, 3], [e.step for e in events[1:]])
finally:
    # Reset to default state for other tests.
    summary_ops.set_step(None)
