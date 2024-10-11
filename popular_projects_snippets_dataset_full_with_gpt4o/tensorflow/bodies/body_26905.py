# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
"""Checks that CsvDataset is equiv to TextLineDataset->map(decode_csv)."""
dataset_actual, dataset_expected = self._make_test_datasets(
    inputs, **kwargs)
self.assertDatasetsEqual(dataset_actual, dataset_expected)
