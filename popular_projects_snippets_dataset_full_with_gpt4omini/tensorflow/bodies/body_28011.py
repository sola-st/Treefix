# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
dataset = dataset_ops.Dataset.range(num_elements).repeat(num_epochs)
if num_outputs:
    range_dataset = dataset_ops.Dataset.range(num_outputs)
    dataset = dataset_ops.Dataset.zip((dataset, range_dataset))
if options:
    dataset = dataset.with_options(options)
exit(dataset)
