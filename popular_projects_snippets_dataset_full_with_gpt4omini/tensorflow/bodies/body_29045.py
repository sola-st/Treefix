# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

# We write a copy of the snapshot first.
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(
    snapshot.legacy_snapshot(
        tmpdir, mode="write", snapshot_name="my_custom_snapshot"))
self.assertDatasetProduces(dataset, list(range(10)))

# We move the run to a new name.
shutil.move(
    os.path.join(tmpdir, "custom-my_custom_snapshot"),
    os.path.join(tmpdir, "custom-my_custom_snapshot_2"))

# Even though the snapshot.metadata is pointing to the old run that no
# longer exists after we moved, we force it to read from the run we specify.
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(
    snapshot.legacy_snapshot(
        tmpdir, mode="read", snapshot_name="my_custom_snapshot_2"))
self.assertDatasetProduces(dataset, list(range(10)))

# We should still have one snapshot and one run.
self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)
