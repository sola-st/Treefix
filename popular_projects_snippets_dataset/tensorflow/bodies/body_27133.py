# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/snapshot_ft_test.py
super().setUp()
self._path = os.path.join(
    tempfile.mkdtemp(dir=self.get_temp_dir()),
    "snapshot_ft_test",
)
