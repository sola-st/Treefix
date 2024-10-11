# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
exit(dataset_ops.Dataset.range(10).map(_map_fn).apply(
    interleave_ops.parallel_interleave(_interleave_fn, 1)))
