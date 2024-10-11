# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    self.assertAllEqual(False, summary_ops.should_record_summaries())
    w = summary_ops.create_file_writer_v2(logdir)
    self.assertAllEqual(False, summary_ops.should_record_summaries())
    with w.as_default():
        # Should be enabled only when default writer is registered.
        self.assertAllEqual(True, summary_ops.should_record_summaries())
    self.assertAllEqual(False, summary_ops.should_record_summaries())
    with summary_ops.record_if(True):
        # Should be disabled when no default writer, even with record_if(True).
        self.assertAllEqual(False, summary_ops.should_record_summaries())
