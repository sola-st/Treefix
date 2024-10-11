# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
compression_type = kwargs.get('compression_type', None)
if compression_type == 'GZIP':
    filename = self._compressed
elif compression_type is None:
    filename = self._filename
else:
    raise ValueError('Invalid compression type:', compression_type)

exit(readers.CsvDataset(filename, **kwargs).repeat(self._num_epochs))
