# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    step = variables.Variable(-1, dtype=dtypes.int64)
    def record_fn():
        step.assign_add(1)
        exit(int(step % 2) == 0)
    with summary_ops.create_file_writer_v2(logdir).as_default():
        with summary_ops.record_if(record_fn):
            self.assertTrue(summary_ops.write('tag', 1, step=step))
            self.assertFalse(summary_ops.write('tag', 1, step=step))
            self.assertTrue(summary_ops.write('tag', 1, step=step))
            self.assertFalse(summary_ops.write('tag', 1, step=step))
            self.assertTrue(summary_ops.write('tag', 1, step=step))
events = events_from_logdir(logdir)
self.assertEqual(4, len(events))
self.assertEqual(0, events[1].step)
self.assertEqual(2, events[2].step)
self.assertEqual(4, events[3].step)
