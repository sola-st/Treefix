# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
element_structure, batch_size, expected_batched_structure = y
exit(x + combinations.combine(
    element_structure=element_structure,
    batch_size=batch_size,
    expected_batched_structure=expected_batched_structure))
