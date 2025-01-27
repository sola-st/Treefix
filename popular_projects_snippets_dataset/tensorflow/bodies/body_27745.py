# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
datasets = [
    dataset_ops.Dataset.from_tensors(i).repeat(None)
    for i in range(len(probs))
]
dataset = dataset_ops.Dataset.sample_from_datasets(
    datasets, probs, seed=1813)
dataset = dataset.take(num_samples)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
