# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
dataset = dataset_ops.Dataset.range(10)
exit(test_call(dataset))
