# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
unbatched_structure = nest.map_structure(
    lambda component_spec: component_spec._unbatch(), element_structure)
self.assertEqual(unbatched_structure, expected_unbatched_structure)
