# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
super(SnapshotTest, self).tearDown()
shutil.rmtree(self._snapshot_dir)
