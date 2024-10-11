# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
batched_structure = nest.map_structure(
    lambda component_spec: component_spec._batch(batch_size),
    element_structure)
self.assertEqual(batched_structure, expected_batched_structure)
