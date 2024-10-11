# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
for inputs_expected in ({"inputs": [], "expected": []},
                        {"inputs": 3, "expected": [()]},
                        {"inputs": [3], "expected": [(0,)]},
                        {"inputs": {"a": 3}, "expected": [("a",)]},
                        {"inputs": {"a": {"b": 4}},
                         "expected": [("a", "b")]},
                        {"inputs": [{"a": 2}], "expected": [(0, "a")]},
                        {"inputs": [{"a": [2]}], "expected": [(0, "a", 0)]},
                        {"inputs": [{"a": [(23, 42)]}],
                         "expected": [(0, "a", 0, 0), (0, "a", 0, 1)]},
                        {"inputs": [{"a": ([23], 42)}],
                         "expected": [(0, "a", 0, 0), (0, "a", 1)]},
                        {"inputs": {"a": {"a": 2}, "c": [[[4]]]},
                         "expected": [("a", "a"), ("c", 0, 0, 0)]},
                        {"inputs": {"0": [{"1": 23}]},
                         "expected": [("0", 0, "1")]}):
    inputs = inputs_expected["inputs"]
    expected = inputs_expected["expected"]
    self.assertEqual(list(nest.yield_flat_paths(inputs)), expected)
