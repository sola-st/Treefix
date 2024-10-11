# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset1 = dataset_ops.Dataset.range(0, 1000)
dataset2 = dataset_ops.Dataset.range(1000, 2000)
dataset3 = dataset_ops.Dataset.range(2000, 3000)
dataset4 = dataset_ops.Dataset.range(3000, 4000)

dataset = dataset_ops.Dataset.zip((dataset1, dataset2, dataset3, dataset4))
dataset = dataset.snapshot(path=self._snapshot_dir)

expected = list(
    zip(
        range(0, 1000), range(1000, 2000), range(2000, 3000),
        range(3000, 4000)))
self.assertDatasetProduces(dataset, expected)
self.assertSnapshotDirectoryContains(
    self._snapshot_dir,
    num_fingerprints=1,
    num_runs_per_fingerprint=1,
    num_snapshot_shards_per_run=multiprocessing.cpu_count())
