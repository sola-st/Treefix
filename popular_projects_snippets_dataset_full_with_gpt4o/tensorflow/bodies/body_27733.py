# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
# Sampling skips the first dataset after it becomes empty.
weights = _get_weights_of_type(np.asarray([.5, .1, .4]), weights_type)
datasets = [
    dataset_ops.Dataset.from_tensors(np.int64(-1)),
    dataset_ops.Dataset.from_tensors(np.int64(1)).repeat(),
    dataset_ops.Dataset.range(10).repeat()
]
sample_dataset = dataset_ops.Dataset.sample_from_datasets(
    datasets, weights=weights, stop_on_empty_dataset=False).take(100)

samples_list = self.getIteratorOutput(self.getNext(
    sample_dataset, requires_initialization=True))
self.assertLen(samples_list, 100)
self.assertEqual(samples_list.count(-1), 1)
