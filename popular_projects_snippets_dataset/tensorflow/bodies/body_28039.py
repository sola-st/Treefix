# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(components)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
