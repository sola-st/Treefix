# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/fixed_length_record_dataset_test.py
test_filenames = self._createFiles()
dataset = readers.FixedLengthRecordDataset(
    test_filenames,
    self._record_bytes + 1,  # Incorrect record length.
    self._header_bytes,
    self._footer_bytes,
    buffer_size=10)
self.assertDatasetProduces(
    dataset,
    expected_error=(
        errors.InvalidArgumentError,
        r"Excluding the header \(5 bytes\) and footer \(2 bytes\), input "
        r"file \".*fixed_length_record.0.txt\" has body length 21 bytes, "
        r"which is not an exact multiple of the record length \(4 bytes\).")
    )
