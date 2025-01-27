# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(logdir)
    @def_function.function
    def f():
        with writer.as_default():
            # Use assertAllEqual instead of assertTrue since it works in a defun.
            self.assertAllEqual(summary_ops.write('default', 1, step=0), True)
            with summary_ops.record_if(True):
                self.assertAllEqual(summary_ops.write('set_on', 1, step=0), True)
            with summary_ops.record_if(False):
                self.assertAllEqual(summary_ops.write('set_off', 1, step=0), False)
    f()
events = events_from_logdir(logdir)
self.assertEqual(3, len(events))
self.assertEqual('default', events[1].summary.value[0].tag)
self.assertEqual('set_on', events[2].summary.value[0].tag)
