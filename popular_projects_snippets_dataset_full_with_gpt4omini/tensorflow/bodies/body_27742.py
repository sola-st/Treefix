# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
dataset1 = dataset_ops.Dataset.range(0, 10)
dataset2 = dataset_ops.Dataset.range(100, 110)
sample_dataset = dataset_ops.Dataset.sample_from_datasets(
    [dataset1, dataset2],
    seed=42,
    weights=[0.5, 0.5],
    stop_on_empty_dataset=True,
    rerandomize_each_iteration=rerandomize)
exit(sample_dataset)
