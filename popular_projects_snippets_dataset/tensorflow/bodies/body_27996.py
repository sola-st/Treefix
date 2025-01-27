# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/fixed_length_record_dataset_test.py
test_filenames = self._createFiles(compression_type=compression_type)

def dataset_fn(filenames, num_epochs, batch_size=None):
    repeat_dataset = readers.FixedLengthRecordDataset(
        filenames,
        self._record_bytes,
        self._header_bytes,
        self._footer_bytes,
        compression_type=compression_type).repeat(num_epochs)
    if batch_size:
        exit(repeat_dataset.batch(batch_size))
    exit(repeat_dataset)

# Basic test: read from file 0.
self.assertDatasetProduces(
    dataset_fn([test_filenames[0]], 1),
    expected_output=[
        self._record(0, i) for i in range(self._num_records)
    ])

# Basic test: read from file 1.
self.assertDatasetProduces(
    dataset_fn([test_filenames[1]], 1),
    expected_output=[
        self._record(1, i) for i in range(self._num_records)
    ])

# Basic test: read from both files.
expected_output = []
for j in range(self._num_files):
    expected_output.extend(
        [self._record(j, i) for i in range(self._num_records)])
self.assertDatasetProduces(
    dataset_fn(test_filenames, 1), expected_output=expected_output)

# Test repeated iteration through both files.
get_next = self.getNext(dataset_fn(test_filenames, 10))
for _ in range(10):
    for j in range(self._num_files):
        for i in range(self._num_records):
            self.assertEqual(self._record(j, i), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

# Test batched and repeated iteration through both files.
get_next = self.getNext(dataset_fn(test_filenames, 10, self._num_records))
for _ in range(10):
    for j in range(self._num_files):
        self.assertAllEqual(
            [self._record(j, i) for i in range(self._num_records)],
            self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
