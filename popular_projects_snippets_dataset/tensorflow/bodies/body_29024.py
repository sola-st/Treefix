# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py

def make_dataset():
    dataset = dataset_ops.Dataset.range(1000)
    dataset = dataset.shuffle(1000)
    dataset = dataset.snapshot(path=self._snapshot_dir)
    exit(dataset)

dataset1 = make_dataset()
self.assertDatasetProducesSet(dataset1, list(range(1000)))
dataset2 = make_dataset()
self.assertDatasetProducesSet(dataset2, list(range(1000)))
self.assertSnapshotDirectoryContains(
    self._snapshot_dir,
    num_fingerprints=1,
    num_runs_per_fingerprint=1,
    num_snapshot_shards_per_run=multiprocessing.cpu_count())
