# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset = dataset_ops.Dataset.range(0)
dataset = dataset.snapshot(path=self._snapshot_dir)
self.assertDatasetProduces(dataset, [])
self.assertSnapshotDirectoryContains(
    self._snapshot_dir,
    num_fingerprints=1,
    num_runs_per_fingerprint=1,
    num_snapshot_shards_per_run=0)

dataset2 = dataset_ops.Dataset.range(0)
dataset2 = dataset.snapshot(path=self._snapshot_dir)
self.assertDatasetProduces(dataset2, [])
