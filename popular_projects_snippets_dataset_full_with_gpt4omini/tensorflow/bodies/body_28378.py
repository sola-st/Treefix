# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
dataset = dataset_ops.Dataset.range(100).filter(
    lambda x: math_ops.not_equal(math_ops.mod(x, div), 2))
if options:
    dataset = dataset.with_options(options)
exit(dataset)
