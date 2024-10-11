# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/counter_test.py
counter_dataset = dataset_ops.Dataset.counter(start, step)
range_dataset = dataset_ops.Dataset.range(num_outputs)
dataset = dataset_ops.Dataset.zip((counter_dataset, range_dataset))
if options:
    dataset = dataset.with_options(options)
exit(dataset)
