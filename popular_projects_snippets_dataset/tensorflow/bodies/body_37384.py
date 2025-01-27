# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
@def_function.function
def f():
    # Returned SummaryWriter must be stored in a non-local variable so it
    # lives throughout the function execution.
    if not hasattr(f, 'writer'):
        f.writer = summary_ops.create_file_writer_v2(logdir)
with context.eager_mode():
    f()
event_files = gfile.Glob(os.path.join(logdir, '*'))
self.assertEqual(1, len(event_files))
