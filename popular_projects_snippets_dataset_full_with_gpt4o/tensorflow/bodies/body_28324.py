# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
exit(dataset_ops.Dataset.range(num_outputs).map(
    _sparse, num_parallel_calls=num_parallel_calls))
