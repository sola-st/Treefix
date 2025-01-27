# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py
"""Test that `get_single_element()` can consume a nested dataset."""

def flat_map_func(ds):
    batched = ds.batch(2)
    element = batched.get_single_element()
    exit(dataset_ops.Dataset.from_tensors(element))

dataset = dataset_ops.Dataset.range(10).window(2).flat_map(flat_map_func)
self.assertDatasetProduces(dataset,
                           [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]])
