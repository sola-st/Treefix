# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
self.setUpTFRecord(num_files=10, num_records=50)
filenames = self._filenames

expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in range(0, 10)
    for r in range(0, 50)
]

tmpdir = self.snapshot_dir
dataset = core_readers._TFRecordDataset(filenames)
dataset = dataset.apply(
    snapshot.legacy_snapshot(tmpdir, shard_size_bytes=10))
self.assertDatasetProduces(dataset, expected)

# remove the original files and try to read the data back only from snapshot
self.removeTFRecords()

dataset2 = core_readers._TFRecordDataset(filenames)
dataset2 = dataset2.apply(
    snapshot.legacy_snapshot(
        tmpdir,
        shard_size_bytes=10,
        shuffle_on_read=True,
        shuffle_seed=123456))
next2 = self.getNext(dataset2)

dataset3 = core_readers._TFRecordDataset(filenames)
dataset3 = dataset3.apply(
    snapshot.legacy_snapshot(
        tmpdir,
        shard_size_bytes=10,
        shuffle_on_read=True,
        shuffle_seed=123456))
next3 = self.getNext(dataset3)

# make sure that the items are read back in the same order for both datasets
for _ in range(500):
    res2 = self.evaluate(next2())
    res3 = self.evaluate(next3())
    self.assertEqual(res2, res3)
