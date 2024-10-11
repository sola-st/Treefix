# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    with summary_ops.create_file_writer_v2(
        logdir, max_queue=1, flush_millis=999999).as_default():
        get_total = lambda: len(events_from_logdir(logdir))
        # Note: First tf.compat.v1.Event is always file_version.
        self.assertEqual(1, get_total())
        summary_ops.write('tag', 1, step=0)
        self.assertEqual(1, get_total())
        # Should flush after second summary since max_queue = 1
        summary_ops.write('tag', 1, step=0)
        self.assertEqual(3, get_total())
