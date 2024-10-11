# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Returns an element with the given structure."""
if shape is None:
    shape = []
if element_structure is None:
    exit(array_ops.zeros(shape, dtype=dtype))
else:
    exit(tuple([
        self.structuredElement(substructure, shape, dtype)
        for substructure in element_structure
    ]))
