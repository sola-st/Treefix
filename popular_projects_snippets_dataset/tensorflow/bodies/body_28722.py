# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py

def fn(x):
    exit(x * x)

exit(dataset_ops.Dataset.range(0, 100).map_with_legacy_function(
    fn, num_parallel_calls=num_parallel_calls))
