# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
l = type_([1, 2, 3])
with self.assertRaisesRegex(
    TypeError,
    "'s' does not have the same nested structure"):
    tf.function(for_with_variable_structure)(l)
