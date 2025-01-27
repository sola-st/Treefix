# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
l = type_([1, 2, 3])
with self.assertRaisesRegex(
    TypeError,
    "'n' has dtype int32 before the loop, but dtype float32 after"):
    tf.function(for_with_variable_dtype_and_early_stopping)(l)
