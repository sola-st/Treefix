# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
self.setUpTFRecord(5, 500)
filenames = self._filenames

expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in range(0, 5)
    for r in range(0, 500)
]

tmpdir = self.snapshot_dir
dataset = core_readers._TFRecordDataset(filenames)
dataset = dataset.apply(
    snapshot.legacy_snapshot(
        tmpdir,
        shard_size_bytes=1024 * 1024,
        num_reader_threads=2,
        reader_buffer_size=10,
        compression=compression))
self.assertDatasetProduces(dataset, expected, assert_items_equal=True)

# remove the original files and try to read the data back only from
# snapshot.
self.removeTFRecords()

dataset2 = core_readers._TFRecordDataset(filenames)
dataset2 = dataset2.apply(
    snapshot.legacy_snapshot(
        tmpdir,
        shard_size_bytes=1024 * 1024,
        num_reader_threads=2,
        reader_buffer_size=10,
        compression=compression))
self.assertDatasetProduces(dataset2, expected, assert_items_equal=True)
