# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset = dataset_ops.Dataset.range(1000)
dataset = dataset.enumerate()
dataset = dataset.snapshot(
    path=self._snapshot_dir, shard_func=lambda i, _: i % 2)
dataset = dataset.map(lambda _, elem: elem)
self.assertDatasetProduces(dataset, list(range(1000)))
self.assertSnapshotDirectoryContains(
    self._snapshot_dir,
    num_fingerprints=1,
    num_runs_per_fingerprint=1,
    num_snapshot_shards_per_run=2)
