# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_batched_features_dataset_test.py
features = {
    "file": parsing_ops.FixedLenFeature([], dtypes.int64),
    "record": parsing_ops.FixedLenFeature([], dtypes.int64),
}
dataset = (
    core_readers.TFRecordDataset(self._filenames)
    .map(lambda x: parsing_ops.parse_single_example(x, features))
    .repeat(10).batch(2))
next_element = self.getNext(dataset)
for file_batch, _, _, _, record_batch, _ in self._next_expected_batch(
    range(self._num_files), 2, 10):
    actual_batch = self.evaluate(next_element())
    self.assertAllEqual(file_batch, actual_batch["file"])
    self.assertAllEqual(record_batch, actual_batch["record"])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element())
