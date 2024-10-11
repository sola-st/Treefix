# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
dataset = dataset_ops.Dataset.range(20).filter(
    lambda x: math_ops.equal(x % 2, 0)).cache()
expected = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
self.verifyRandomAccess(dataset, expected)
