# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
exit(dataset_ops.Dataset.range(10).map(_map_fn).flat_map(_flat_map_fn))
