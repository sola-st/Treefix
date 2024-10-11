# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/range_test.py
dataset = dataset_ops.Dataset.range(start, stop)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
