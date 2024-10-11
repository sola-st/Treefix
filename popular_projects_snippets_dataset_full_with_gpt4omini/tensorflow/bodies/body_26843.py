# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
dataset = dataset_ops.Dataset.from_tensors(42).filter(
    lambda x: True, name="filter")
self.assertDatasetProduces(dataset, [42])
