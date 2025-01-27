# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

# We create two iterators but call getNext on only one.
dataset1 = dataset_ops.Dataset.range(1000)
dataset1 = dataset1.apply(snapshot.legacy_snapshot(tmpdir))
next1 = self.getNext(dataset1)

dataset2 = dataset_ops.Dataset.range(1001)
dataset2 = dataset2.apply(snapshot.legacy_snapshot(tmpdir))
_ = self.getNext(dataset2)

for _ in range(1000):
    self.evaluate(next1())

# We check that only one directory is created.
self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)
