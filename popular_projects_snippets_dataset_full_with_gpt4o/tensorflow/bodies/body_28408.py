# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(components).repeat(-1)
dataset = dataset.group_by_window(
    key_func=lambda x: x % 3,
    reduce_func=lambda _, xs: xs.batch(4),
    window_size=4)
exit(dataset)
