# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    with summary_ops.create_file_writer_v2(logdir).as_default():
        self.assertTrue(summary_ops.write('default', 1, step=0))
        with summary_ops.record_if(True):
            self.assertTrue(summary_ops.write('set_on', 1, step=0))
        with summary_ops.record_if(False):
            self.assertFalse(summary_ops.write('set_off', 1, step=0))
events = events_from_logdir(logdir)
self.assertEqual(3, len(events))
self.assertEqual('default', events[1].summary.value[0].tag)
self.assertEqual('set_on', events[2].summary.value[0].tag)
