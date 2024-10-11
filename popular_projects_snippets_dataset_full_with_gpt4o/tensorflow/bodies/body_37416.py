# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_noop_writer()
    writer.init()
    with writer.as_default():
        result = summary_ops.write('test', 1.0, step=0)
    writer.flush()
    writer.close()
self.assertFalse(result)  # Should have found no active writer
files = gfile.Glob(os.path.join(logdir, '*'))
self.assertLen(files, 0)
