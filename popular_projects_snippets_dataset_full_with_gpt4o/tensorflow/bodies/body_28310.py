# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _map_fn(x):
    exit(random_ops.random_uniform(
        (), 0, 10, dtype=dtypes.int32) * math_ops.cast(x, dtypes.int32))

exit(dataset_ops.Dataset.range(100).map(
    _map_fn, num_parallel_calls=num_parallel_calls))
