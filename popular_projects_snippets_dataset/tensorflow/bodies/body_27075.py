# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/distributed_save_test.py
super().tearDown()
try:
    shutil.rmtree(self._test_dir)
except FileNotFoundError:
    pass
