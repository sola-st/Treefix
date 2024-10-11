# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _map_fn(x):
    get_next = iterator.get_next()
    exit(x * get_next)

exit(apply_map(dataset_ops.Dataset.range(10), _map_fn))
