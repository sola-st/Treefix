# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py
dataset = dataset_ops.Dataset.range(100).prefetch(10)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
