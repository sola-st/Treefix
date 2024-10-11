# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
dataset = dataset_ops.Dataset.range(42).window(6).interleave(
    lambda x: x, cycle_length=2, num_parallel_calls=2)
exit(dataset)
