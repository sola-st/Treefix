# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(
        logdir, max_queue=1000, flush_millis=1000000)
    get_total = lambda: len(events_from_logdir(logdir))
    self.assertEqual(1, get_total())  # file_version Event
    # Calling init() again while writer is open has no effect
    writer.init()
    self.assertEqual(1, get_total())
    with writer.as_default():
        summary_ops.write('tag', 1, step=0)
        self.assertEqual(1, get_total())
        # Calling .close() should do an implicit flush
        writer.close()
        self.assertEqual(2, get_total())
