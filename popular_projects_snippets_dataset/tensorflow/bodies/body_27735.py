# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
weights = _get_weights_of_type(np.asarray([1., 0.]), weights_type)
datasets = [
    dataset_ops.Dataset.range(0),
    dataset_ops.Dataset.range(1).repeat()
]
sample_dataset = dataset_ops.Dataset.sample_from_datasets(
    datasets, weights=weights, stop_on_empty_dataset=True)
self.assertDatasetProduces(sample_dataset, [],
                           requires_initialization=True)
