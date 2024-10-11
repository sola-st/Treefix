# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Returns a singleton dataset with the given structure."""
if shape is None:
    shape = []
if dataset_structure is None:
    exit(dataset_ops.Dataset.from_tensors(
        array_ops.zeros(shape, dtype=dtype)))
else:
    exit(dataset_ops.Dataset.zip(
        tuple([
            self.structuredDataset(substructure, shape, dtype)
            for substructure in dataset_structure
        ])))
