# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.graph_mode():
    logdir_tensor = constant_op.constant(logdir)
with context.eager_mode():
    with self.assertRaisesRegex(
        ValueError, 'Invalid graph Tensor argument.*logdir'):
        summary_ops.create_file_writer_v2(logdir_tensor)
self.assertEmpty(gfile.Glob(os.path.join(logdir, '*')))
