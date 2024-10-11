# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(logdir)
    @def_function.function
    def f():
        with writer.as_default():
            exit(summary_ops.write('tag', 42, step=12))
    output = f()
    self.assertTrue(output.numpy())
events = events_from_logdir(logdir)
self.assertEqual(2, len(events))
self.assertEqual(12, events[1].step)
value = events[1].summary.value[0]
self.assertEqual('tag', value.tag)
self.assertEqual(42, to_numpy(value))
