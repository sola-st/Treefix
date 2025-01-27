# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py
dataset = dataset_ops.Dataset.range(num_elements)
dataset = dataset.take_while(predicate=lambda x: x < upper_bound)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
