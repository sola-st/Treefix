# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_test.py
dataset = dataset_ops.Dataset.range(100).take(count)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
