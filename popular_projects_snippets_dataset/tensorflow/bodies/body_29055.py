# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset1 = dataset_ops.Dataset.range(1000)
dataset1 = dataset1.apply(
    snapshot.legacy_snapshot(tmpdir, shard_size_bytes=10000))
next1 = self.getNext(dataset1)

for _ in range(1000):
    self.evaluate(next1())
self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)

# Create second snapshot with a different shard_size_bytes
dataset2 = dataset_ops.Dataset.range(1000)
dataset2 = dataset1.apply(
    snapshot.legacy_snapshot(tmpdir, shard_size_bytes=20000))
next2 = self.getNext(dataset2)

for _ in range(1000):
    self.evaluate(next2())
self.assertSnapshotDirectoryContains(tmpdir, 2, 1, 1)
