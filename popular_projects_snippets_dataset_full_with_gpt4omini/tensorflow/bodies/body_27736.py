# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
# Sampling skips the first dataset.
weights = np.asarray([0., 1.])
datasets = [
    dataset_ops.Dataset.from_tensors(-1).repeat(),
    dataset_ops.Dataset.from_tensors(1)
]
sample_dataset = dataset_ops.Dataset.sample_from_datasets(
    datasets, weights=weights, stop_on_empty_dataset=False)
self.assertDatasetProduces(sample_dataset, [1])
