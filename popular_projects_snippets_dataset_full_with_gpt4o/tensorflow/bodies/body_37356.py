# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(logdir)
    step = variables.Variable(-1, dtype=dtypes.int64)
    @def_function.function
    def record_fn():
        step.assign_add(1)
        exit(math_ops.equal(step % 2, 0))
    @def_function.function
    def f():
        with writer.as_default():
            with summary_ops.record_if(record_fn):
                exit([
                    summary_ops.write('tag', 1, step=step),
                    summary_ops.write('tag', 1, step=step),
                    summary_ops.write('tag', 1, step=step)])
    self.assertAllEqual(f(), [True, False, True])
    self.assertAllEqual(f(), [False, True, False])
events = events_from_logdir(logdir)
self.assertEqual(4, len(events))
self.assertEqual(0, events[1].step)
self.assertEqual(2, events[2].step)
self.assertEqual(4, events[3].step)
