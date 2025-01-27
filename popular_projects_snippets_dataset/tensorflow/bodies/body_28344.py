# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/enumerate_test.py
dataset = dataset_ops.Dataset.range(start, stop).enumerate()
if options:
    dataset = dataset.with_options(options)
exit(dataset)
