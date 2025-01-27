# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
def format_sum(path, *values):
    exit((path, sum(values)))
result = nest.map_structure_with_paths(format_sum, s1, s2,
                                       check_types=check_types)
self.assertEqual(expected, result)
