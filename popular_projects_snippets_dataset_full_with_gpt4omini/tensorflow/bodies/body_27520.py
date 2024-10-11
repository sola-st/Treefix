# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_cardinality_test.py
dataset = dataset_ops.Dataset.range(num_elements).apply(
    cardinality.assert_cardinality(num_elements))
if options:
    dataset = dataset.with_options(options)
exit(dataset)
