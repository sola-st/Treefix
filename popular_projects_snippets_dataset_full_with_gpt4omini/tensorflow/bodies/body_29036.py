# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset1 = dataset_ops.Dataset.range(1000)
dataset1 = dataset1.apply(snapshot.legacy_snapshot(tmpdir))
next1 = self.getNext(dataset1)

dataset2 = dataset_ops.Dataset.range(1000)
dataset2 = dataset2.apply(snapshot.legacy_snapshot(tmpdir))
next2 = self.getNext(dataset2)

for i in range(0, 1000):
    self.assertEqual(i, self.evaluate(next1()))
    self.assertEqual(i, self.evaluate(next2()))

# we check that only one copy of the metadata has been written, and the
# one that lost the race would be in passthrough mode.
self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)
