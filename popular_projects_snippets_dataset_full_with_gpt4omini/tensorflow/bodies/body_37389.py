# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
@def_function.function
def f():
    with summary_ops.create_file_writer_v2(logdir).as_default():
        pass  # Calling .as_default() is enough to indicate use.
with context.eager_mode():
    # TODO(nickfelt): change this to a better error
    with self.assertRaisesRegex(
        errors.NotFoundError, 'Resource.*does not exist'):
        f()
    # Even though we didn't use it, an event file will have been created.
self.assertEqual(1, len(gfile.Glob(os.path.join(logdir, '*'))))
