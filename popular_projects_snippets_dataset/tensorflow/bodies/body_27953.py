# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = array_ops.identity(dataset)
exit(dataset)
