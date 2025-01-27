# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
# Note: a user function without a top-level function scope should
# never be found in user code; it's only possible in generated code.
exit(py_builtins.globals_in_original_context(test_scope))
