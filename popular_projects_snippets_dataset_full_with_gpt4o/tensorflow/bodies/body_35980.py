# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.assertRaisesRegex(ValueError, r"custom_getter .* not callable:"):
    with variable_scope.variable_scope("scope0", custom_getter=3):
        variable_scope.get_variable("name0")
with self.assertRaisesRegex(ValueError, r"custom_getter .* not callable:"):
    variable_scope.get_variable("name0", custom_getter=3)
