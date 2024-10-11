# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
# Testing that one dataset can create multiple iterators fine.
# `repeat` creates multiple iterators from the same C++ Dataset.
record_defaults = [[0]] * 4
inputs = [['1,,3,4', '5,6,,8']]
ds_actual, ds_expected = self._make_test_datasets(
    inputs, record_defaults=record_defaults)
self.assertDatasetsEqual(
    ds_actual.repeat(5).prefetch(1),
    ds_expected.repeat(5).prefetch(1))
