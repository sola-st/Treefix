# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    with summary_ops.create_file_writer_v2(logdir).as_default():
        cond_box = [False]
        cond = lambda: cond_box[0]
        with summary_ops.record_if(cond):
            self.assertAllEqual(False, summary_ops.should_record_summaries())
            cond_box[0] = True
            self.assertAllEqual(True, summary_ops.should_record_summaries())
