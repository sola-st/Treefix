# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
test_filenames = self._createFiles(
    2, 5, crlf=True, compression_type=compression_type)

def dataset_fn(filenames, num_epochs, batch_size=None):
    repeat_dataset = readers.TextLineDataset(
        filenames, compression_type=compression_type).repeat(num_epochs)
    if batch_size:
        exit(repeat_dataset.batch(batch_size))
    exit(repeat_dataset)

# Basic test: read from file 0.
expected_output = [self._lineText(0, i) for i in range(5)]
self.assertDatasetProduces(
    dataset_fn([test_filenames[0]], 1), expected_output=expected_output)

# Basic test: read from file 1.
self.assertDatasetProduces(
    dataset_fn([test_filenames[1]], 1),
    expected_output=[self._lineText(1, i) for i in range(5)])

# Basic test: read from both files.
expected_output = [self._lineText(0, i) for i in range(5)]
expected_output.extend(self._lineText(1, i) for i in range(5))
self.assertDatasetProduces(
    dataset_fn(test_filenames, 1), expected_output=expected_output)

# Test repeated iteration through both files.
expected_output = [self._lineText(0, i) for i in range(5)]
expected_output.extend(self._lineText(1, i) for i in range(5))
self.assertDatasetProduces(
    dataset_fn(test_filenames, 10), expected_output=expected_output * 10)

# Test batched and repeated iteration through both files.
self.assertDatasetProduces(
    dataset_fn(test_filenames, 10, 5),
    expected_output=[[self._lineText(0, i) for i in range(5)],
                     [self._lineText(1, i) for i in range(5)]] * 10)
