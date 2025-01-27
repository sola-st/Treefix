# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py

def do_test(i):
    dataset = dataset_ops.Dataset.range(10).cache(self.cache_prefix)
    get_next = self.getNext(dataset)
    for _ in range(i):
        try:
            self.evaluate(get_next())
        except errors.OutOfRangeError:
            break

if not context.executing_eagerly():
    self.skipTest(
        "Test requires eager mode for iterators to be deconstructed")

for i in [0, 3, 10, 12, 15]:
    do_test(i)
