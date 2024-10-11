# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/distributed_save_test.py
super().setUp()
self._test_dir = os.path.join(
    tempfile.mkdtemp(dir=self.get_temp_dir()),
    "distributed_save_test",
)
