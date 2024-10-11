# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
"""Test a dataset that represents a dataset."""
dataset = dataset_ops.Dataset.from_tensors(dataset_ops.Dataset.range(10))
dataset = dataset.flat_map(lambda x: x)
self.assertDatasetProduces(dataset, expected_output=range(10))
