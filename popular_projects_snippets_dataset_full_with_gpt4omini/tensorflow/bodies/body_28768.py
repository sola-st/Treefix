# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset = dataset_ops.Dataset.range(10)
iterator = iter(dataset)
for _ in range(10):
    queue.enqueue(next(iterator))
