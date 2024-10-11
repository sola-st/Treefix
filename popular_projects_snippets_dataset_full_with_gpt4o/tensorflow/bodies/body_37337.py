# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    with summary_ops.create_file_writer_v2(logdir).as_default():
        with summary_ops.record_if(False):
            self.assertFalse(summary_ops.write('tag', 42))
