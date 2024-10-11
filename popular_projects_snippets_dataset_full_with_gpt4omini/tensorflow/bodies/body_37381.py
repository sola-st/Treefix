# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    with self.subTest(name='has_writer'):
        with summary_ops.create_file_writer_v2(logdir).as_default():
            self.assertTrue(summary_ops.has_default_writer())
    with self.subTest(name='no_writer'):
        self.assertFalse(summary_ops.has_default_writer())
