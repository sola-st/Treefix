# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset1 = dataset_ops.Dataset.range(1000)
dataset1 = dataset1.apply(
    snapshot.legacy_snapshot(tmpdir, pending_snapshot_expiry_seconds=1))
next1 = self.getNext(dataset1)

# Don't finish reading dataset1, so it is never finalized
for _ in range(500):
    self.evaluate(next1())
self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)

time.sleep(2)

# Creating dataset2 after we run through dataset1 due to eager mode, where
# the snapshot state is determined immediately upon dataset creation. We
# only want to determine the snapshot state for dataset2 after the first
# snapshot has expired.
dataset2 = dataset_ops.Dataset.range(1000)
dataset2 = dataset2.apply(
    snapshot.legacy_snapshot(tmpdir, pending_snapshot_expiry_seconds=1))
next2 = self.getNext(dataset2)

for _ in range(500):
    self.evaluate(next2())
self.assertSnapshotDirectoryContains(tmpdir, 1, 2, 1)
