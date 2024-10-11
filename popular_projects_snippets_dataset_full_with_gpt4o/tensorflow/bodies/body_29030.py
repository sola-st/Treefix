# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
super(LegacySnapshotTest, self).tearDown()
shutil.rmtree(self.snapshot_dir)
