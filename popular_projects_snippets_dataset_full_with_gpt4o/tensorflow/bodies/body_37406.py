# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
try:
    import psutil  # pylint: disable=g-import-not-at-top
except ImportError:
    raise unittest.SkipTest('test requires psutil')
proc = psutil.Process()
get_open_filenames = lambda: set(info[0] for info in proc.open_files())
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(logdir)
    files = gfile.Glob(os.path.join(logdir, '*'))
    self.assertEqual(1, len(files))
    eventfile = files[0]
    self.assertIn(eventfile, get_open_filenames())
    del writer
    self.assertNotIn(eventfile, get_open_filenames())
