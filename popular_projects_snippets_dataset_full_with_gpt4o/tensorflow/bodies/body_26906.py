# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
"""Checks that elements produced by CsvDataset match expected output."""
# Convert str type because py3 tf strings are bytestrings
filenames = self._setup_files(inputs, linebreak, compression_type)
kwargs['compression_type'] = compression_type
if expected_err_re is not None:
    # Verify that OpError is produced as expected
    with self.assertRaisesOpError(expected_err_re):
        dataset = readers.CsvDataset(filenames, **kwargs)
        self.getDatasetOutput(dataset)
else:
    dataset = readers.CsvDataset(filenames, **kwargs)
    expected_output = [
        tuple(v.encode('utf-8') if isinstance(v, str) else v
              for v in op)
        for op in expected_output
    ]
    self.assertDatasetProduces(dataset, expected_output)
