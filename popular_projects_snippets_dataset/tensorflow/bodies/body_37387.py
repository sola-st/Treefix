# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
@def_function.function
def f():
    summary_ops.create_file_writer_v2(constant_op.constant(logdir))
with context.eager_mode():
    with self.assertRaisesRegex(
        ValueError, 'Invalid graph Tensor argument.*logdir'):
        f()
self.assertEmpty(gfile.Glob(os.path.join(logdir, '*')))
