# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/choose_from_datasets_test.py
datasets = [
    dataset_ops.Dataset.range(num_elements_per_dataset)
    for _ in range(num_datasets)
]
indices = []
for i in range(num_datasets):
    indices = indices + ([i] * num_elements_per_dataset)
shuffled_indices = stateless_random_ops.stateless_shuffle(
    np.int64(indices), seed=[1, 2])
choice_dataset = dataset_ops.Dataset.from_tensor_slices(shuffled_indices)
dataset = dataset_ops.Dataset.choose_from_datasets(datasets, choice_dataset)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
