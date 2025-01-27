# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
exit(dataset_ops.Dataset.range(10).map(_map_fn).interleave(
    _interleave_fn, cycle_length=1))
