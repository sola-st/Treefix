# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/choose_from_datasets_test.py
datasets = [
    dataset_ops.Dataset.from_tensors(b"foo").repeat(),
    dataset_ops.Dataset.from_tensors(b"bar").repeat(),
    dataset_ops.Dataset.from_tensors(b"baz").repeat(),
]
dataset = dataset_ops.Dataset.choose_from_datasets(
    datasets,
    choice_dataset=dataset_ops.Dataset.range(0),
    stop_on_empty_dataset=False)
self.assertDatasetProduces(dataset, [])
