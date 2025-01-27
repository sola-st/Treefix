# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset = dataset_ops.Dataset.range(1000)
dataset = dataset.apply(
    snapshot.legacy_snapshot(tmpdir, compression=compression))
self.assertDatasetProduces(dataset, list(range(1000)))

self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)
