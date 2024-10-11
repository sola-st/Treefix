# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
self.setUpTFRecord()
filenames = self._filenames

expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in range(0, 10)
    for r in range(0, 10)
]

tmpdir = self.snapshot_dir
dataset = core_readers._TFRecordDataset(filenames)
dataset = dataset.apply(
    snapshot.legacy_snapshot(tmpdir, compression=compression))
self.assertDatasetProduces(dataset, expected)

# remove the original files and try to read the data back only from snapshot
self.removeTFRecords()

dataset2 = core_readers._TFRecordDataset(filenames)
dataset2 = dataset2.apply(
    snapshot.legacy_snapshot(tmpdir, compression=compression))
self.assertDatasetProduces(dataset2, expected)
