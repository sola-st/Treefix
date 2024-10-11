# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py

def map_fn(y):
    exit(10 * math_ops.cast(y, dtypes.int32))

exit(dataset_ops.Dataset.range(100).map(map_fn))
