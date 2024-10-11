# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
# Sampling stops when the second dataset is exhausted.
weights = _get_weights_of_type(np.asarray([0., 1.]), weights_type)
datasets = [
    dataset_ops.Dataset.from_tensors(-1).repeat(2),
    dataset_ops.Dataset.from_tensors(1).repeat(2)
]
sample_dataset = dataset_ops.Dataset.sample_from_datasets(
    datasets, weights=weights, stop_on_empty_dataset=True)
self.assertDatasetProduces(sample_dataset, [1, 1],
                           requires_initialization=True)
