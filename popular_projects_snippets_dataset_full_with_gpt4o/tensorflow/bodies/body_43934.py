# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
l = list_type(n)
self.assertFunctionMatchesEager(for_with_variable_shape_growing_vector, l)
