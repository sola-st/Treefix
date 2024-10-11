# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
dataset = dataset_ops.Dataset.range(10).cache(self.cache_prefix)
get_next = self.getNext(dataset)
for _ in range(i):
    try:
        self.evaluate(get_next())
    except errors.OutOfRangeError:
        break
