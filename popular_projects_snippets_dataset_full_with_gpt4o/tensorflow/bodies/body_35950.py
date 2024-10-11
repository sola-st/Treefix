# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
"""get_{local,}variable() must take the same list of args."""
arg_names = tf_inspect.getargspec(variable_scope.get_variable)[0]
local_arg_names = tf_inspect.getargspec(
    variable_scope.get_local_variable)[0]
self.assertEqual(arg_names, local_arg_names)
