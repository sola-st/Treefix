# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/fixed_length_record_dataset_test.py
filenames = self._createFiles()
exit(readers.FixedLengthRecordDataset(
    filenames, self._record_bytes, self._header_bytes,
    self._footer_bytes).repeat(num_epochs))
