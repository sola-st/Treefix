# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
get_total = lambda: len(events_from_logdir(logdir))
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(
        logdir, max_queue=1000, flush_millis=1000000)
    self.assertEqual(1, get_total())  # file_version Event
    with writer.as_default():
        summary_ops.write('tag', 1, step=0)
        self.assertEqual(1, get_total())
        writer.flush()
        self.assertEqual(2, get_total())
        summary_ops.write('tag', 1, step=0)
        self.assertEqual(2, get_total())
    # Exiting the "as_default()" should do an implicit flush
    self.assertEqual(3, get_total())
