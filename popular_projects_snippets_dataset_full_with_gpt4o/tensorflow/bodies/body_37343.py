# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
try:
    with context.graph_mode():
        writer = summary_ops.create_file_writer_v2(logdir)
        summary_ops.set_step(1)
        with writer.as_default():
            write_op = summary_ops.write('tag', 1.0)
        summary_ops.set_step(2)
        with self.cached_session() as sess:
            sess.run(writer.init())
            sess.run(write_op)
            sess.run(write_op)
            sess.run(writer.flush())
    events = events_from_logdir(logdir)
    self.assertEqual(3, len(events))
    self.assertEqual(1, events[1].step)
    # The step value will still be 1 because the value was captured at the
    # time the graph was constructed.
    self.assertEqual(1, events[2].step)
finally:
    # Reset to default state for other tests.
    summary_ops.set_step(None)
