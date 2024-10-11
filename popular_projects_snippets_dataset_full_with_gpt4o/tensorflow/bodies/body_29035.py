# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset = dataset_ops.Dataset.range(1000)
dataset = dataset.apply(snapshot.legacy_snapshot(tmpdir))
self.assertDatasetProduces(dataset, list(range(1000)))

dataset = dataset_ops.Dataset.range(1001)
dataset = dataset.apply(snapshot.legacy_snapshot(tmpdir))
self.assertDatasetProduces(dataset, list(range(1001)))

self.assertSnapshotDirectoryContains(tmpdir, 2, 1, 1)
