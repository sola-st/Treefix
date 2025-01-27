# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset1 = dataset_ops.Dataset.range(1000)
dataset1 = dataset1.snapshot(path=self._snapshot_dir)
self.assertDatasetProduces(dataset1, list(range(1000)))

dataset2 = dataset_ops.Dataset.range(2000)
dataset2 = dataset2.snapshot(path=self._snapshot_dir)
self.assertDatasetProduces(dataset2, list(range(2000)))

self.assertSnapshotDirectoryContains(
    self._snapshot_dir,
    num_fingerprints=2,
    num_runs_per_fingerprint=1,
    num_snapshot_shards_per_run=multiprocessing.cpu_count())
