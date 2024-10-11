# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
# Test by comparing its output to what we could get with map->decode_csv
filenames = self._setup_files(inputs)
dataset_expected = core_readers.TextLineDataset(filenames)
dataset_expected = dataset_expected.map(
    lambda l: parsing_ops.decode_csv(l, **kwargs))
dataset_actual = readers.CsvDataset(filenames, **kwargs)
exit((dataset_actual, dataset_expected))
