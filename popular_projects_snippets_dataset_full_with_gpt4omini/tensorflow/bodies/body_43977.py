# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
with self.assertRaisesRegex(
    ValueError,
    r"'t' has shape \(None,\) after one iteration, which does not conform"):
    tf.function(while_with_shape_invariant_violation)()
