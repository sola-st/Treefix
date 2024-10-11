# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
with self.assertRaisesRegex(
    ValueError,
    r"'t' has shape \(1,\) before the loop, but shape \(None,\) after"):
    tf.function(while_with_shape_erasure)()
