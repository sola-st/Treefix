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
    snapshot.legacy_snapshot(tmpdir, shard_size_bytes=100))
self.assertDatasetProduces(dataset, expected)

# remove the original files and try to read the data back only from snapshot
self.removeTFRecords()

dataset2 = core_readers._TFRecordDataset(filenames)
dataset2 = dataset2.apply(
    snapshot.legacy_snapshot(
        tmpdir, shard_size_bytes=100, shuffle_on_read=True))
shuffled_elements = self.getDatasetOutput(dataset2)
# make sure that we don't read the file back in the same order.
self.assertNotEqual(shuffled_elements, expected)
self.assertCountEqual(shuffled_elements, expected)

# make sure all the elements are still there
dataset3 = core_readers._TFRecordDataset(filenames)
dataset3 = dataset3.apply(
    snapshot.legacy_snapshot(
        tmpdir, shard_size_bytes=100, shuffle_on_read=True))
self.assertDatasetProduces(dataset3, expected, assert_items_equal=True)
