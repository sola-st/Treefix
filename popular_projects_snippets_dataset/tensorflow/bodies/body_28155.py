# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unique_test.py
exit(dataset_ops.Dataset.range(num_elements).map(
    lambda x: x % unique_elem_range).unique())
