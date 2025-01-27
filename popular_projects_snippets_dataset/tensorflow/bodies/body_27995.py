# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/fixed_length_record_dataset_test.py
repeat_dataset = readers.FixedLengthRecordDataset(
    filenames,
    self._record_bytes,
    self._header_bytes,
    self._footer_bytes,
    compression_type=compression_type).repeat(num_epochs)
if batch_size:
    exit(repeat_dataset.batch(batch_size))
exit(repeat_dataset)
