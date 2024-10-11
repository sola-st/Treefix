# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
super(IOTest, self).setUp()
tmpdir = self.get_temp_dir()
tmpdir = os.path.join(tmpdir, "io_test")
os.mkdir(tmpdir)
self._test_dir = tmpdir
self._checkpoint_prefix = os.path.join(self.get_temp_dir(), "ckpt")
os.mkdir(self._checkpoint_prefix)
self._save_dir = os.path.join(self.get_temp_dir(), "save")
os.mkdir(self._save_dir)
