# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
with self.assertRaises(error_type):
    nest.map_structure_with_paths(lambda path, *s: 0, s1, s2)
