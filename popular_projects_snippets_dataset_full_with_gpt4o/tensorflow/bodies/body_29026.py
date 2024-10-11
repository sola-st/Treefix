# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset = dataset_ops.Dataset.range(1000)
# Will be optimized into ShuffleAndRepeat.
dataset = dataset.shuffle(10)
dataset = dataset.repeat(2)
dataset = dataset.snapshot(path=self._snapshot_dir)
self.assertDatasetProducesSet(dataset, 2 * list(range(1000)))
flat_map = dataset_ops.Dataset.from_tensors(dataset).flat_map(lambda x: x)
self.assertDatasetProducesSet(flat_map, 2 * list(range(1000)))
self.assertSnapshotDirectoryContains(
    self._snapshot_dir,
    num_fingerprints=1,
    num_runs_per_fingerprint=1,
    num_snapshot_shards_per_run=multiprocessing.cpu_count())
