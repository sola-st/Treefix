# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
super(LegacySnapshotTest, self).setUp()
self.removeTFRecords()
tmpdir = self.get_temp_dir()
tmpdir = os.path.join(tmpdir, "snapshot")
os.mkdir(tmpdir)
self.snapshot_dir = tmpdir
