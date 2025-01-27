# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.assertRaisesRegex(
    ValueError,
    "The initializer passed is not valid. It should be a callable with no "
    "arguments and the shape should not be provided or an instance of "
    "`tf.keras.initializers.*' and `shape` should be fully defined."):
    variable_scope.get_variable("foo", initializer=lambda x: [2])
