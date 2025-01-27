# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
ds = dataset_ops.Dataset.range(0)
exit(next(iter(ds)))
