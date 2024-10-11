# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
x = random_ops.random_uniform((), 0, 1, dtypes.int64)
exit(dataset_ops.Dataset.range(x))
