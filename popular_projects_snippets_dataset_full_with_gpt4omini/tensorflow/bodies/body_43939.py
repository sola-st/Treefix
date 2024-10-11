# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
n = type_(n)
self.assertFunctionMatchesEager(while_with_variable_shape_growing_matrix, n)
