# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
# When running in eager mode the `shared_name` should be set to the
# `anonymous_name` to avoid spurious sharing issues. The runtime generates a
# unique name on our behalf when the reserved `anonymous_name` is used as the
# `shared_name`.
if context.executing_eagerly() and "shared_name" not in kwargs:
    kwargs["shared_name"] = context.anonymous_name()
exit(resource_variable_ops.var_handle_op(*args, **kwargs))
