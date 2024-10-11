# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
self.createTFRecords()
filenames = self._filenames
expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in range(0, 10)
    for r in range(0, 100)
]

dataset = core_readers._TFRecordDataset(filenames)
dataset = dataset.snapshot(
    path=self._snapshot_dir,
    reader_func=(
        lambda ds: ds.interleave(  # pylint:disable=g-long-lambda
            lambda x: x,
            cycle_length=4,
            num_parallel_calls=4)))
self.assertDatasetProduces(dataset, expected)
self.assertSnapshotDirectoryContains(
    self._snapshot_dir,
    num_fingerprints=1,
    num_runs_per_fingerprint=1,
    num_snapshot_shards_per_run=multiprocessing.cpu_count())

self.removeTFRecords()
dataset2 = core_readers._TFRecordDataset(filenames)
dataset2 = dataset2.snapshot(
    self._snapshot_dir,
    reader_func=(
        lambda ds: ds.interleave(  # pylint:disable=g-long-lambda
            lambda x: x,
            cycle_length=4,
            num_parallel_calls=4)))
self.assertDatasetProducesSet(dataset2, expected)
