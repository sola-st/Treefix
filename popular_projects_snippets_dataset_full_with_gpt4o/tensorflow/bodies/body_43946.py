# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
n = type_(n)
self.assertFunctionMatchesEager(
    while_with_composite_tensor_shape_invariant, n)
