# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
n = type_(n)
self.assertFunctionMatchesEager(for_with_nested_variable_shape_inside_if, n)
