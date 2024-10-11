# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
ds = dataset_ops.Dataset.range(20).apply(
    shuffle_ops.shuffle_and_repeat(buffer_size=21))
get_next = self.getNext(ds)
self.evaluate(get_next())
