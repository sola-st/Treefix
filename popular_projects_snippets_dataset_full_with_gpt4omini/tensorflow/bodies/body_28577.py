# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
cache_path = self.cache_prefix + "_" + str(i)
exit(dataset_ops.Dataset.range(100).shuffle(100).cache(cache_path))
