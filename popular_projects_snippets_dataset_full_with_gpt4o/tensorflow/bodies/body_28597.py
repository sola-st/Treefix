# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
exit(dataset_ops.Dataset.range(self.range_size).cache(filename).repeat(
    self.num_repeats))
