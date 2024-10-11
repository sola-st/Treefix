# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(
    snapshot.legacy_snapshot(tmpdir, compression=compression))
dataset = dataset.repeat(10)
self.assertDatasetProduces(dataset, list(range(10)) * 10)

self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)
