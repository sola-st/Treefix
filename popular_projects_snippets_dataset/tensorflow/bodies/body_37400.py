# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(
        logdir, max_queue=999999, flush_millis=999999)
    with writer.as_default():
        get_total = lambda: len(events_from_logdir(logdir))
        # Note: First tf.compat.v1.Event is always file_version.
        self.assertEqual(1, get_total())
        summary_ops.write('tag', 1, step=0)
        summary_ops.write('tag', 1, step=0)
        self.assertEqual(1, get_total())
        summary_ops.flush()
        self.assertEqual(3, get_total())
        # Test "writer" parameter
        summary_ops.write('tag', 1, step=0)
        self.assertEqual(3, get_total())
        summary_ops.flush(writer=writer)
        self.assertEqual(4, get_total())
