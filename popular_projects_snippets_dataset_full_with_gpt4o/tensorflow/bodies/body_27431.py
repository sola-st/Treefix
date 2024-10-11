# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
"""Checks that elements produced by CsvDataset match expected output."""
# Convert str type because py3 tf strings are bytestrings
filenames = self._setup_files(
    inputs,
    compression_type=kwargs.get("compression_type", None),
    encoding=encoding)
dataset = self._make_csv_dataset(
    filenames,
    batch_size=batch_size,
    num_epochs=num_epochs,
    label_name=label_name,
    encoding=encoding,
    **kwargs)
self._verify_output(dataset, batch_size, num_epochs, label_name,
                    expected_output, expected_keys)
