# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    for _ in range(10):
        summary_ops.create_file_writer_v2(logdir)
event_files = gfile.Glob(os.path.join(logdir, '*'))
self.assertLen(event_files, 10)
