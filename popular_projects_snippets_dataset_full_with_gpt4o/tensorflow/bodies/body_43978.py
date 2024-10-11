# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
l = type_([1, 2, 3])
with self.assertRaisesRegex(
    ValueError,
    r"'t' has shape \(None,\) after one iteration, which does not conform"):
    tf.function(for_with_shape_invariant_violation)(l)
