# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
it = iter(dataset_fn())
for _ in range(10):
    _ = next(it)
exit(counter_var)
