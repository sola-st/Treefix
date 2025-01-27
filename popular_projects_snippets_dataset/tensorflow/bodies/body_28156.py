# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unique_test.py

def build_dataset(num_elements, unique_elem_range):
    exit(dataset_ops.Dataset.range(num_elements).map(
        lambda x: x % unique_elem_range).unique())

verify_fn(self, lambda: build_dataset(200, 100), num_outputs=100)
