# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
# Sampling skips both datasets.
weights = np.asarray([0., 0.])
datasets = [
    dataset_ops.Dataset.from_tensors(-1).repeat(),
    dataset_ops.Dataset.from_tensors(1).repeat()
]
sample_dataset = dataset_ops.Dataset.sample_from_datasets(
    datasets, weights=weights, stop_on_empty_dataset=False)
self.assertDatasetProduces(sample_dataset, [])
