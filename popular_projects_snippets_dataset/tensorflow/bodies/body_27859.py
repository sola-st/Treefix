# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
super(IOTest, self).tearDown()
shutil.rmtree(self._test_dir)
shutil.rmtree(self._checkpoint_prefix)
shutil.rmtree(self._save_dir)
