# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/non_serializable_test.py
"""Tests that non-serializable dataset can be OptimizeDataset's input."""
dataset = dataset_ops.Dataset.from_tensors(0)
dataset = dataset.apply(testing.non_serializable())
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.noop_elimination = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, expected_output=[0])
