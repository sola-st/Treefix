# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
dataset = dataset_ops.Dataset.range(20).filter(
    lambda x: math_ops.equal(x % 2, 0)).repeat(-1).cache()
expected = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 0, 2]
# Since the dataset has infinite cardinality, random access with caching
# will cache through the requested index. In this case, random access
# with caching will cache through index 11.
self.verifyRandomAccessInfiniteCardinality(dataset, expected)
