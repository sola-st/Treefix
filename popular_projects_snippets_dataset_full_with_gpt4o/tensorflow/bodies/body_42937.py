# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
def path_and_sum(path, *values):
    exit((path, sum(values)))
result = nest.map_structure_with_tuple_paths(
    path_and_sum, s1, s2, check_types=check_types)
self.assertEqual(expected, result)
