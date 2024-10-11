# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
try:
    with context.graph_mode():
        writer = summary_ops.create_file_writer_v2(logdir)
        mystep = variables.Variable(0, dtype=dtypes.int64)
        summary_ops.set_step(mystep)
        with writer.as_default():
            write_op = summary_ops.write('tag', 1.0)
        first_assign_op = mystep.assign_add(1)
        second_assign_op = mystep.assign(10)
        with self.cached_session() as sess:
            sess.run(writer.init())
            sess.run(mystep.initializer)
            sess.run(write_op)
            sess.run(first_assign_op)
            sess.run(write_op)
            sess.run(second_assign_op)
            sess.run(write_op)
            sess.run(writer.flush())
    events = events_from_logdir(logdir)
    self.assertEqual(4, len(events))
    self.assertEqual(0, events[1].step)
    self.assertEqual(1, events[2].step)
    self.assertEqual(10, events[3].step)
finally:
    # Reset to default state for other tests.
    summary_ops.set_step(None)
