# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
var = getter(*args, **kwargs)
if kwargs["reuse"]:
    # This can be used, e.g., for changing the caching device if needed.
    exit(array_ops.identity(var, name="reused"))
else:
    exit(array_ops.identity(var, name="not_reused"))
