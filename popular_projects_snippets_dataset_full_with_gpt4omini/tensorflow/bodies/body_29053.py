# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset1 = dataset_ops.Dataset.range(0, 100)
dataset2 = dataset_ops.Dataset.range(100, 200)
dataset3 = dataset_ops.Dataset.range(200, 300)

dataset = dataset1.concatenate(dataset2).concatenate(dataset3)
dataset = dataset.apply(snapshot.legacy_snapshot(tmpdir))
self.assertDatasetProduces(dataset, list(range(300)))

dataset4 = dataset_ops.Dataset.range(200, 300)
dataset5 = dataset_ops.Dataset.range(100, 200)
dataset6 = dataset_ops.Dataset.range(0, 100)

dataset = dataset6.concatenate(dataset5).concatenate(dataset4)
dataset = dataset.apply(snapshot.legacy_snapshot(tmpdir))
self.assertDatasetProduces(dataset, list(range(300)))

self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)
