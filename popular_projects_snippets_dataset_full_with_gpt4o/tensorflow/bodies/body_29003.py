# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
super(SnapshotTest, self).setUp()
tmpdir = self.get_temp_dir()
tmpdir = os.path.join(tmpdir, "snapshot")
os.mkdir(tmpdir)
self._snapshot_dir = tmpdir
