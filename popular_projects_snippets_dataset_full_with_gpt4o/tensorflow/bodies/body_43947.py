# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
l = type_(n)
self.assertFunctionMatchesEager(
    for_with_composite_tensor_shape_invariant, l)
