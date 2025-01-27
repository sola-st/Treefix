# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py

dataset = dataset_ops.Dataset.range(10).group_by_window(
    key_func=lambda x: x,
    reduce_func=lambda _, window: window.batch(1),
    window_size=1)
self.assertDatasetProduces(
    dataset, expected_output=[[i] for i in range(10)])
