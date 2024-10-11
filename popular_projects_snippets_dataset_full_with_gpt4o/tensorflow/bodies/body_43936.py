# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
l = type_(l)
self.assertFunctionMatchesEager(
    for_with_variable_shape_growing_matrix_rows, l)
